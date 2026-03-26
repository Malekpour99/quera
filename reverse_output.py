# https://quera.org/problemset/3405
# ---------------------------------

nums: list[int] = []

n = int(input().strip())

while n != 0:
    nums.append(n)
    n = int(input().strip())

for _ in range(len(nums)):
    print(nums.pop())
