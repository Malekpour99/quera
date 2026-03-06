import threading
import pickle
import os
from typing import Callable
from collections import defaultdict


class OlympicsServer:
    def __init__(self):
        self.lock = threading.Lock()  # Map: topic_pattern -> list of callbacks
        self.subscriptions = defaultdict(list)  # Store undelivered QoS 1 messages
        self.pending_messages = []  # List: Tuple(topic: str, message: str)
        self.storage_file = "messages.pkl"  # Storage file

        # Load pending messages
        self._load_pending_messages()

    def _load_pending_messages(self):
        """Load pending messages from pickle file"""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "rb") as f:
                self.pending_messages = pickle.load(f)
        else:
            self.pending_messages = []

    def _save_pending_messages(self):
        """Save pending messages to pickle file"""
        with open(self.storage_file, "wb") as f:
            pickle.dump(self.pending_messages, f)

    def _topic_matches(self, subscription: str, published_topic: str) -> bool:
        """
        Check if published topic matches subscription pattern.
        subscription pattern can contain:
        - + for single level wildcard
        - # for multi-level wildcard (must be at the end)
        """
        sub_parts = subscription.split("/")
        pub_parts = published_topic.split("/")

        # Special case: subscription ends with #
        if subscription.endswith("/#"):
            # Remove the # from parts
            sub_parts = sub_parts[:-1]
            # Check if published topic starts with subscription prefix
            if len(pub_parts) < len(sub_parts):
                return False
            for i in range(len(sub_parts)):
                if sub_parts[i] != "+" and sub_parts[i] != pub_parts[i]:
                    return False
            return True

        # For patterns without # at the end, lengths must match
        if len(sub_parts) != len(pub_parts):
            return False

        for i in range(len(sub_parts)):
            if sub_parts[i] == "+":
                continue
            elif sub_parts[i] == "#":
                # can only be at the end in proper MQTT
                return i == len(sub_parts) - 1
            elif sub_parts[i] != pub_parts[i]:
                return False

        return True

    def publish(self, topic: str, message: str, qos: int):
        """Publish message to topic with given QoS"""

        def publish_task():
            with self.lock:
                # Find all matching subscriptions
                delivered = False

                for sub_pattern, callbacks in self.subscriptions.items():
                    if self._topic_matches(sub_pattern, topic):
                        for callback in callbacks:
                            try:
                                callback(topic, message)
                                delivered = True
                            except Exception:
                                pass

                # For QoS 1, if not delivered to anyone, store it
                if qos == 1 and not delivered:
                    self.pending_messages.append((topic, message))
                    self._save_pending_messages()

        # Run in thread
        thread = threading.Thread(target=publish_task, daemon=True)
        thread.start()
        thread.join()

    def subscribe(self, topic: str, callback: Callable):
        """Subscribe to a topic"""
        with self.lock:
            # Add to subscriptions
            self.subscriptions[topic].append(callback)

            # Check for pending messages that match
            messages_to_remove = []

            for i, msg in enumerate(self.pending_messages):
                if self._topic_matches(topic, msg[0]):
                    # Deliver pending message
                    try:
                        callback(msg[0], msg[1])
                    except Exception:
                        pass
                    messages_to_remove.append(i)

            # Remove delivered messages (from end to beginning)
            for i in sorted(messages_to_remove, reverse=True):
                del self.pending_messages[i]

            # Save updated pending messages
            if messages_to_remove:
                self._save_pending_messages()
