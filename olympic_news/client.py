from typing import Callable
from server import OlympicsServer


class Publisher:
    def __init__(self, server: OlympicsServer):
        self.server = server

    def publish(self, topic: str, message: str, qos: int):
        """Publish a message through the server"""
        self.server.publish(topic, message, qos)


class Subscriber:
    def __init__(self, server: OlympicsServer, callback: Callable):
        self.server = server
        self.callback = callback

    def subscribe(self, topic: str):
        """Subscribe to a topic through the server"""
        self.server.subscribe(topic, self.callback)


class Client:
    def __init__(self, server: OlympicsServer):
        self.server = server

    def publish(self, topic: str, message: str, qos: int):
        """Publish a message"""
        publisher = Publisher(self.server)
        publisher.publish(topic, message, qos)

    def subscribe(self, topic: str, callback: Callable):
        """Subscribe to a topic"""
        subscriber = Subscriber(self.server, callback)
        subscriber.subscribe(topic)
