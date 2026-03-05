import random
import string

from base import Base
from packet import Packet
from receiver import Receiver


class Transmitter(Base):
    def __init__(self, key: str, bait_count: int = 2, chunk_size: int = 3):
        self._key = key
        self.bait_count = bait_count
        self.chunk_size = chunk_size

    def transmit(self, message: str, receiver: Receiver) -> list[Packet]:
        # prepare packets
        packets = self._prepare_packets(message)

        # send packets to receiver
        receiver.receive(packets)

        return packets

    def _prepare_packets(self, message: str) -> list[Packet]:
        # prepare real data packets
        packets: list[Packet] = []
        sequence_count: int = 1
        for i in range(0, len(message), self.chunk_size):
            data = message[i: i + self.chunk_size]
            packets.append(
                Packet(
                    sequence_number=sequence_count,
                    data=data,
                    hashed_data=self._hash_function(data, self._key),
                )
            )

            sequence_count += 1

        # add bait packets after real data packets
        self._add_bait_packets(packets)

        # shuffle packets
        random.shuffle(packets)

        return packets

    def _add_bait_packets(self, packets: list) -> None:
        letters_digits = string.ascii_letters + string.digits  # a-zA-Z0-9
        sequence_count = len(packets) + 1
        for _ in range(self.bait_count):
            random_string = "".join(
                random.choice(letters_digits)
                for _ in range(random.randint(1, self.chunk_size))
            )
            packets.append(
                Packet(
                    sequence_number=sequence_count,
                    data=random_string,
                    hashed_data=self._unused_hash(random_string),
                )
            )
