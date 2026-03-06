# https://quera.org/problemset/251439?tab=description
# ---------------------------------------------------

from client import Client
from server import OlympicsServer


def message_callback(topic, message):
    print(f"Received message on topic {topic}: {message}")


# Create server and client
server = OlympicsServer()
client = Client(server)

# Subscribe with multi-level wildcard
client.subscribe("sports/#", message_callback)

# Publish messages
client.publish("sports/football", "Football match result: Team A won!", qos=1)
client.publish("sports/football/worldcup", "World Cup result: Team Z won!", qos=1)
client.publish("sports/basketball/nba", "NBA result: Team Y won!", qos=1)
