# https://quera.org/problemset/1359
# ---------------------------------

pairs_count = int(input().strip())


def is_order_preserved(*, base_string: str, search_string: str) -> bool:
    """
    Check whether order of search_string characters
    are preserved in the base_string or not
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


for _ in range(pairs_count):
    base_string = input().strip()
    search_string = input().strip()

    # check initial order
    is_initial_order_preserved = is_order_preserved(
        base_string=base_string,
        search_string=search_string,
    )

    # check reverse order in-case initial order was not preserved
    if not is_initial_order_preserved:
        is_reverse_order_preserved = is_order_preserved(
            base_string=base_string,
            search_string=search_string[::-1],
        )

    if is_initial_order_preserved or is_reverse_order_preserved:
        print("YES")
    else:
        print("NO")
