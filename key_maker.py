# https://quera.org/problemset/6314
# ---------------------------------

while True:
    depths_count, keys_count = map(int, input().strip().split())

    # handling 0 0 terminated input
    if depths_count == 0 and keys_count == 0:
        exit()

    matched_keys: int = 0
    main_key = list(map(int, input().strip().split()))

    for _ in range(keys_count):
        can_be_matched: bool = True
        sample_key = list(map(int, input().strip().split()))
        for i in range(depths_count):
            if sample_key[i] > main_key[i]:
                can_be_matched = False
                break

        if can_be_matched:
            matched_keys += 1
        else:
            continue

    print(matched_keys)
