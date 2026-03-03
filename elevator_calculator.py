# https://quera.org/problemset/175884
# -----------------------------------
BUTTON_MAPPER = {
    "U": 1,  # Up button
    "D": -1,  # Down button
}


def calculate_floor(string: str) -> int:
    floor = 0
    for btn in string:
        floor += BUTTON_MAPPER.get(btn, 0)
    return floor
