from dataclasses import dataclass
from typing import Callable


@dataclass
class Packet:
    sequence_number: int
    data: str
    hashed_data: str

    def is_valid(self, hash_func: Callable, key: str) -> bool:
        return self.hashed_data == hash_func(self.data, key)

    def __repr__(self):
        return self.data
