# https://quera.org/problemset/145008
# -----------------------------------

from typing import Annotated, Literal, Final

FORK: Final = "F"
SPOON: Final = "S"
FULL_SETUP: Final = {FORK, SPOON}

SpoonFork = Annotated[str, Literal[FORK, SPOON]]

plates_count = int(input().strip())
spoon_and_forks = input().strip()

# zero-indexed
plates: dict[int, set[SpoonFork]] = {i: set() for i in range(plates_count)}

for i, tool in enumerate(spoon_and_forks):
    plate = i % plates_count
    plates[plate].add(tool)

# keep track of every plate having one spoon and one fork
has_full_setup: bool = True

for tools in plates.values():
    if tools != FULL_SETUP:
        has_full_setup = False
        break

if has_full_setup:
    print("YES")
else:
    print("NO")
