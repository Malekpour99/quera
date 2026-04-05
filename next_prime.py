# https://quera.org/problemset/593
# --------------------------------

from math import ceil, sqrt

base = int(input().strip())

current_num = base + 1 if base % 2 == 0 else base + 2
current_prime: int = 2  # just as initial value (smallest prime number)
seem_prime_count: int = 0
next_prime_count: int = 0

while base > 0:
    next_prime_count += base % 10
    base = base // 10

while seem_prime_count != next_prime_count:
    found_prime = True
    for i in range(3, ceil(sqrt(current_num)) + 1, 2):
        if current_num % i == 0:
            found_prime = False
            break

    if found_prime:
        current_prime = current_num
        seem_prime_count += 1

    current_num += 2

print(current_prime)
