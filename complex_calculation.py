# https://quera.org/problemset/279
# --------------------------------

a, x, n = map(int, input().strip().split())

# based on the Binomial Theorem
sum_: int = (a + x) ** n

print(sum_)
