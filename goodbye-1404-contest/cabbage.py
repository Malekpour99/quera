n = int(input().strip())
for _ in range(n):
    cabbages_count = int(input().strip())
    cabbages_list = list(map(int, input().strip().split()))
    split_count = 0
    if cabbages_count < 2:
        print(split_count)
        continue
    else:
        max_allowed_length = cabbages_list[0] * 2 - 1
        for cabbage in cabbages_list[1:]:
            pieces = (cabbage + max_allowed_length - 1) // max_allowed_length
            split_count += (pieces - 1)

        print(split_count)
