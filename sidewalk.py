# https://quera.org/problemset/104590
# -----------------------------------

tiles_count, queries_count = map(int, input().strip().split())
tiles = list(map(int, input().strip().split()))  # zero-indexed

# For solving queries in O(1), we group tiles which can be traveled together
# group_id[i] represents the alternating segment(group) ID that house i belongs to
current_group: int = 0
group_id: list[int] = [current_group] * tiles_count

for i in range(1, tiles_count):
    if tiles[i] == tiles[i - 1]:
        # Color is same as previous, sequence breaks, new group
        current_group += 1

    # Else: Color is different, continues in the same group
    group_id[i] = current_group

for _ in range(queries_count):
    start, end = map(int, input().strip().split())
    start_index = start - 1
    end_index = end - 1
    if group_id[start_index] == group_id[end_index]:
        print("YES")
    else:
        print("NO")
