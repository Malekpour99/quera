# https://quera.org/problemset/9595
# ---------------------------------

n = int(input().strip())

major_mistake_counts: int = 0

for _ in range(n):
    line_1 = input().strip().replace(" ", "")
    line_2 = input().strip().replace(" ", "")

    if len(line_1) != len(line_2):
        major_mistake_counts += 1

print(major_mistake_counts)
