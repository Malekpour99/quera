# https://quera.org/problemset/187843
# -----------------------------------

n, m = map(int, input().strip().split())

length_counter = 1
is_returning = False  # whether we are returning from end of row or not

for _ in range(n):
    if is_returning:
        for i in range(length_counter + m - 1, length_counter - 1, -1):
            print(i, end=" ")
    else:
        for i in range(length_counter, length_counter + m, 1):
            print(i, end=" ")

    print("")
    length_counter += m
    is_returning = not is_returning
