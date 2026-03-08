# https://quera.org/problemset/76277
# ----------------------------------

from dataclasses import dataclass
from typing import Literal

TimeFormatType = Literal[
    "dd/mm/yyyy‍",
    "dd/yyyy‍/mm",
    "yyyy‍/mm/dd",
    "yyyy‍/dd/mm",
    "‍‍mm/yyyy‍/dd",
    "‍‍mm/dd/yyyy‍",
]


def extract_time_key(time_format: TimeFormatType, time: str) -> int:
    format_strings = time_format.split("/")
    time_strings = time.split("/")
    for i, fmt in enumerate(format_strings):
        if fmt == "dd":
            day = time_strings[i]
        if fmt == "mm":
            month = time_strings[i]
        if fmt == "yyyy":
            year = time_strings[i]

    return int(year + month + day)


@dataclass
class Factor:
    time_format: TimeFormatType
    time: str
    time_key: int  # Time integer value: YYYYMMDD
    value: int

    def __str__(self) -> str:
        return f"{self.time} - {self.value}"

    def __repr__(self):
        return str(self)


class FactorHandler:
    def __init__(self) -> None:
        self.submitted_factors: list[Factor] = []

    def add_factor(self, time_format: TimeFormatType, time: str, value: int) -> None:
        self.submitted_factors.append(
            Factor(
                time_format=time_format,
                time=time,
                time_key=extract_time_key(time_format, time),
                value=value,
            )
        )

    def remove_all_factors(self, time_format: TimeFormatType, time: str) -> None:
        remove_time_key = extract_time_key(time_format, time)
        self.submitted_factors = [
            factor
            for factor in self.submitted_factors
            if factor.time_key != remove_time_key
        ]

    def get_sum(
        self,
        time_format: TimeFormatType,
        start_time: str,
        finish_time: str,
    ) -> int:
        total_sum = 0
        start_time_key = extract_time_key(time_format, start_time)
        finish_time_key = extract_time_key(time_format, finish_time)
        for factor in self.submitted_factors:
            if start_time_key <= factor.time_key <= finish_time_key:
                total_sum += factor.value

        return total_sum
