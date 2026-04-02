# https://quera.org/problemset/140031
# -----------------------------------

num_str = input().strip()

sum: int = 0

for digit in num_str:
    if digit.isdigit():
        sum += int(digit)

print(sum)
