# https://quera.org/problemset/209100
# -----------------------------------

cases = int(input().strip())

for _ in range(cases):
    pairs_count = int(input().strip())
    pairs: list[str] = input().strip().split()

    index: int = 0
    mismatch_count: int = 0

    while mismatch_count <= 2 and index < pairs_count * 2:
        if pairs[index][1:] != pairs[index + 1][1:]:
            mismatch_count += 1

        index += 2

    if mismatch_count > 2:
        print("NO")
    else:
        print("YES")
