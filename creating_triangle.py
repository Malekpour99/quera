# https://quera.org/problemset/280
# --------------------------------

a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

if (a * a == b * b + c * c) or (b * b == a * a + c * c) or (c * c == a * a + b * b):
    print("YES")
else:
    print("NO")
