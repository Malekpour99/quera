# https://quera.org/problemset/265789
# -----------------------------------

n = int(input().strip())
book_prices = list(map(int, input().strip().split()))

book_prices.sort(reverse=True)

cost: int = 0

for i, price in enumerate(book_prices):
    if (i + 1) % 3 != 0:  # Pay for all except every 3rd book
        cost += price

print(cost)
