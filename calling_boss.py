# https://quera.org/problemset/3414
# ---------------------------------

employee_x, employee_y, boss_x, boss_y = map(int, input().strip().split())

if employee_y == boss_y:
    print("Horizontal")
elif employee_x == boss_x:
    print("Vertical")
else:
    print("Try again")
