# https://quera.org/problemset/127289
# -----------------------------------

code_cup_mapper: dict[int, str] = {
    1: "c",
    2: "o",
    3: "d",
    4: "e",
    5: "c",
    6: "u",
    7: "p",
    0: "6",
}

index = int(input().strip())

print(code_cup_mapper.get(index % 8))
