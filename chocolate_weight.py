# https://quera.org/problemset/261557
# -----------------------------------

total, chocolate_per_bisc, biscuits = map(int, input().strip().split())

print(chocolate_per_bisc * (biscuits - 1))
