# https://quera.org/problemset/2529
# ---------------------------------

names_count = int(input().strip())
max_len = 0

for _ in range(names_count):
    name_len = len(set(input().strip()))
    max_len = name_len if name_len > max_len else max_len

print(max_len)
