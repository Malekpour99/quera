# https://quera.org/problemset/147193
# -----------------------------------

a, b = map(int, input().strip().split())

# ax + b = 0 answers:
if a == 0:
    if b == 0:
        print("infinite")
    else:
        print("invalid")  # division by zero
else:
    print("unique")
