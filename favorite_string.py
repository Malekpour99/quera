# https://quera.org/problemset/52546
# ----------------------------------


def is_substring(*, base_string: str, search_string: str) -> bool:
    """
    Check whether search_string can be extracted by
    removing other excessive characters from base_string
    if strings are matched there will be no need to
    remove any characters, and substring condition is true
    """
    order_matched: bool = True
    last_seen_index: int = 0
    i: int = 0
    while i < len(search_string):
        is_found: bool = False
        for j in range(last_seen_index, len(base_string)):
            if search_string[i] == base_string[j] and j >= last_seen_index:
                last_seen_index, is_found = j, True
                break

        if is_found:
            i += 1
        else:
            order_matched = False
            break

    return order_matched


fav_string = input().strip()
strings_count = int(input().strip())

fav_count: int = 0

for _ in range(strings_count):
    input_string = input().strip()
    if is_substring(base_string=input_string, search_string=fav_string):
        fav_count += 1

print(fav_count)
