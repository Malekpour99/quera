# https://quera.org/problemset/102254
# -----------------------------------

from collections import Counter


def compress_number_string(num_str: str) -> str:
    num_count: dict[str, int] = Counter(num_str)

    # considering uniques digits
    next_chars: list[str] = [*num_count.keys()]

    # adding counts >= 2 based on digit counts
    for count in num_count.values():
        if count > 1:
            next_chars.append(str(count))

    next_chars.sort()
    return "".join(next_chars)


current_num_str = input().strip()

while True:
    compressed_num = compress_number_string(current_num_str)
    if current_num_str == compressed_num:
        print(compressed_num)
        break

    current_num_str = compressed_num
