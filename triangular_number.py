# https://quera.org/problemset/66861
# ----------------------------------

from math import sqrt


def count_divisors(num: int) -> int:
    """
    Counts the number of divisors of a given integer num.
    Uses iteration up to sqrt(num) for efficiency.
    """

    count = 0

    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            if i * i == num:
                count += 1
            else:
                count += 2

    return count


number_of_divisors = int(input().strip())

n = 1
while True:
    # Calculate the number of divisors for the n-th triangular number (good number)
    # T(n) = n * (n + 1) / 2
    # n and n+1 are co-prime (meaning: GCD(n, n+1) = 1)

    if n % 2 == 0:
        # n is even: factors are (n/2) and (n+1)
        divisors = count_divisors(n // 2) * count_divisors(n + 1)
    else:
        # n is odd: factors are n and ((n+1)/2)
        divisors = count_divisors(n) * count_divisors((n + 1) // 2)

    if divisors >= number_of_divisors:
        triangular_number = n * (n + 1) // 2
        print(triangular_number)
        break

    n += 1
