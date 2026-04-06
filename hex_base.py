# https://quera.org/problemset/6374
# ---------------------------------

int_to_hex: dict[int, str] = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}

hex_to_int: dict[str, int] = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}

hex_num = input().strip()

incremented_hex_num: str = ""
i = len(hex_num) - 1

while i > -1:
    has_increment: bool = False

    incremented_digit = hex_to_int[hex_num[i]] + 1
    if incremented_digit == 16:
        incremented_digit, has_increment = 0, True

    incremented_hex_num = int_to_hex[incremented_digit] + incremented_hex_num

    if has_increment:
        i -= 1

        if i == -1:
            incremented_hex_num = "1" + incremented_hex_num
    else:
        incremented_hex_num = hex_num[:i] + incremented_hex_num
        break

print(incremented_hex_num)
