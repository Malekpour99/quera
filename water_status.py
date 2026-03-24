# https://quera.org/problemset/3429
# ---------------------------------

t = int(input().strip())

if t > 100:
    print("Steam")
elif t < 0:
    print("Ice")
else:
    print("Water")
