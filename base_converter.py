# https://quera.org/problemset/66859
# ----------------------------------

base_num_mapper: dict[int, str] = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}


def get_digit_string(val: int) -> str:
    if val < 10:
        return str(val)
    else:
        return base_num_mapper.get(val, "?")


n, b = map(int, input().strip().split())

result = ""

while n > 0:
    reminder = n % b
    result = get_digit_string(reminder) + result
    n = n // b

print(result)
