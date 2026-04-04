# https://quera.org/problemset/3029
# ---------------------------------

x, y = map(int, input().strip().split())
x_1, y_1 = map(int, input().strip().split())

if x < x_1:
    print("Right")
else:
    print("Left")
