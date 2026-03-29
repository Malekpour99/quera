# https://quera.org/problemset/146465
# -----------------------------------

chocolate_total, sequence_count = map(int, input().strip().split())

if chocolate_total % sequence_count == 0:
    print("YES")
else:
    print("NO")
