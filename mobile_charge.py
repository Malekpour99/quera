# https://quera.org/problemset/17244
# ----------------------------------

target_charge = int(input().strip())

duration = target_charge * (target_charge + 1) // 2

print(duration)
