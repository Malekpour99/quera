# https://quera.org/problemset/2551
# ---------------------------------


def perform_operation(operation: str, *nums: list[int]) -> int:
    if operation == "+":
        return sum(nums)
    elif operation == "*":
        result: int = 1
        for num in nums:
            result *= num
        return result
    else:
        raise Exception(f"unsupported operation {operation}")


num1 = int(input().strip())
operation = input().strip()
num2 = int(input().strip())

result = perform_operation(operation, num1, num2)

print(result)
