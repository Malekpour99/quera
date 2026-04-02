# https://quera.org/problemset/158165
# -----------------------------------

from collections import OrderedDict
from typing import Final

MEGA_BYTE_SIZE: Final = 1024 * 1024
KILO_BYTE_SIZE: Final = 1024
BYTE_SIZE: Final = 1

MEGA_BYTE_SUFFIX: Final = "MiB"
KILO_BYTE_SUFFIX: Final = "KiB"
BYTE_SUFFIX: Final = "B"

volume_size_mapper: dict[int, str] = OrderedDict(
    {
        MEGA_BYTE_SIZE: MEGA_BYTE_SUFFIX,
        KILO_BYTE_SIZE: KILO_BYTE_SUFFIX,
        BYTE_SIZE: BYTE_SUFFIX,
    }
)


def convert_to_human_readable_volume(volume: int) -> str:
    if volume < 1:
        raise Exception("Volume must be a positive integer")

    compatible_size = BYTE_SIZE
    compatible_suffix = BYTE_SUFFIX

    for size, suffix in volume_size_mapper.items():
        if volume >= size:
            compatible_size = size
            compatible_suffix = suffix
            break

    return f"{volume // compatible_size}{compatible_suffix}"


n = int(input().strip())

volumes: list[str] = []

for _ in range(n):
    volume = int(input().strip())
    readable_volume = convert_to_human_readable_volume(volume)
    volumes.append(readable_volume)

print(*volumes, sep="\n")
