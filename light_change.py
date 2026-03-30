# https://quera.org/problemset/49028
# ----------------------------------

change_status_count: int = 0

n = int(input().strip())
current_status = input().strip()

for _ in range(n - 1):
    status = input().strip()
    if current_status != status:
        change_status_count += 1
        current_status = status

print(change_status_count)
