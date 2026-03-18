# https://quera.org/problemset/235328
# -----------------------------------

employees, cinema_cap = map(int, input().strip().split())
employee_friends = sorted(list(map(int, input().strip().split())))

employee_count = 0
attendee_count = 0

for friends in employee_friends:
    if attendee_count + (friends + 1) > cinema_cap:
        continue

    employee_count += 1
    attendee_count += friends + 1

print(employee_count)
