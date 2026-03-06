# https://quera.org/problemset/60134
# ----------------------------------

from typing import Union
from collections import defaultdict


def fruits(tuple_of_fruits: tuple[dict[str, Union[str, int]]]) -> dict[str, int]:
    good_fruits: dict[str, int] = defaultdict(int)

    for fruit in tuple_of_fruits:
        if (
            fruit["shape"] == "sphere"
            and 300 <= fruit["mass"] <= 600
            and 100 <= fruit["volume"] <= 500
        ):
            good_fruits[fruit["name"]] += 1

    return good_fruits
