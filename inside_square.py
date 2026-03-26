# https://quera.org/problemset/283
# --------------------------------

a = int(input().strip())
b = int(input().strip())

if b >= a:
    print("Wrong order!")
elif (a - b) % 2 != 0:
    print("Wrong difference!")
else:
    diff = (a - b) // 2
    for i in range(1, a + 1):
        if i > diff and i <= a - diff:
            print(("* " * diff) + ("  " * b) + ("* " * diff))
        else:
            print("* " * a)
