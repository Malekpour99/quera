from base import Base
from packet import Packet


class Receiver(Base):
    def __init__(self, key: str):
        self._key = key
        self._valid_packets: list[Packet] = []

    def receive(self, packets: list[Packet]) -> None:
        for packet in packets:
            if packet.is_valid(self._hash_function, self._key):
                self._valid_packets.append(packet)

    def get_message(self) -> str:
        # Correct sorting for packets
        self._valid_packets.sort(key=lambda packet: packet.sequence_number)

        # Extract and concatenate the data from sorted packets
        return "".join(packet.data for packet in self._valid_packets)
