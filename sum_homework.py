# https://quera.org/problemset/271649
# -----------------------------------

n = int(input().strip())

# 1 - brute force: O(n)
# sum_: int = 0
# for i in range(n):
#     if i % 2 != 0:
#         sum_ += i

# 2 - Sum of odd numbers up to n = (n // 2) ^ 2
sum_ = (n // 2) ** 2

print(sum_)
