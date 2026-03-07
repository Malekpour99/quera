# https://quera.org/problemset/252329
# -----------------------------------

import math

number_of_inputs = int(input().strip())
differences = list(int(input().strip()) for _ in range(number_of_inputs))

# First Solution: Correct but not optimized and exceeds test time limit!
# ---------------------------------------------------------------------
# for difference in differences:
#     count = 0
#     i = 1
#     j = i + 1
#     while ((i + 1)**2 - i**2) <= difference:  # Can be simplified to: 2i+1 <= difference
#         current_difference = j**2 - i**2
#         if current_difference < difference:
#             j += 1
#         else:  # current_difference >= difference
#             if current_difference == difference:
#                 count += 1
#             i += 1
#             j = i + 1

#     print(count)

# Second Solution: Optimized
# --------------------------
# b² - a² = n
# (b - a)(b + a) = n
# Where b > a ≥ 1 are integers.

# Let:
# x = b - a (positive integer)
# y = b + a (positive integer)

# Then:
# y > x (since a > 0)
# x and y must have the same parity (both even or both odd) because:
#   a = (y - x)/2 must be integer ⇒ y - x must be even
#   x × y = n

for difference in differences:
    count = 0
    for x in range(1, int(math.sqrt(difference)) + 1):
        if difference % x == 0:
            y = difference // x
            # Check conditions:
            # 1. y > x (since b > a)
            # 2. (x + y) is even (so (y - x)/2 is integer)
            if y > x and (x + y) % 2 == 0:
                count += 1

    print(count)
