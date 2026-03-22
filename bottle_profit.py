# https://quera.org/problemset/72880
# ----------------------------------

a, b, c, d, m = map(int, input().strip().split())

a_profit = m * c
a_price = a + a_profit

b_profit = m * d
b_price = b + b_profit

higher_price = "a" if a_price >= b_price else "b"
higher_profit = "a" if a_profit >= b_profit else "b"

if higher_price == higher_profit:
    print("Eyval baba!")
else:
    print("Naaa, eshtebahe!")
