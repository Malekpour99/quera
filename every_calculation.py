# https://quera.org/problemset/3403
# ---------------------------------

nums: list[int] = []

for _ in range(4):
    nums.append(int(input().strip()))

sum_nums: int = sum(nums)
average: float = sum_nums / len(nums)
max_num: int = max(nums)
min_num: int = min(nums)
product: int = 1

for num in nums:
    product *= num

print(
    f"Sum : {sum_nums:.6f}\n"
    f"Average : {average:.6f}\n"
    f"Product : {product:.6f}\n"
    f"MAX : {max_num:.6f}\n"
    f"MIN : {min_num:.6f}"
)
