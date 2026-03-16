# https://quera.org/problemset/640
# --------------------------------

# Greatest Common Divisor (Ladder Calculation Method)
a = int(input().strip())
b = int(input().strip())

while b != 0:
    a, b = b, a % b

print(abs(a))
