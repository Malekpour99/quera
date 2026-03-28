# https://quera.org/problemset/80651
# ----------------------------------

teams_count: int = 0

for _ in range(3):
    member_with_laptop = int(input().strip())
    member_without_laptop = int(input().strip())

    teams_count += min(member_with_laptop, member_without_laptop)

print(teams_count)
