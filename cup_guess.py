# https://quera.org/problemset/8901
# ---------------------------------

moves, goal_cup = input().strip().split()

for _ in range(int(moves)):
    cup_1, cup_2 = input().strip().split()

    # swapping goal cup place only if it changes
    if goal_cup == cup_1:
        goal_cup = cup_2
    elif goal_cup == cup_2:
        goal_cup = cup_1

print(goal_cup)
