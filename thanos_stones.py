# https://quera.org/problemset/211019
# -----------------------------------

stone_colors: dict[str, str] = {
    "space": "blue",
    "mind": "yellow",
    "reality": "red",
    "power": "purple",
    "time": "green",
    "soul": "orange",
}

stone = input().strip()

print(stone_colors.get(stone))
