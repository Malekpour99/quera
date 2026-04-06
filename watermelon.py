# https://quera.org/problemset/104588
# -----------------------------------

watermelons = list(map(int, input().strip().split()))

count: int = 0
for watermelon in watermelons:
    if watermelon >= 80:
        count += 1

if count >= 3:
    print("Mamma mia!")
elif count > 0:
    print("Mamma mia!!")
else:
    print("Mamma mia!!!")
