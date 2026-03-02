# https://quera.org/problemset/190993?tab=description
# ---------------------------------------------------

UNKNOWN_KEY_MESSAGE = "Unknown"

# Getting Initial Input
nums, queries, length = input().strip().split()
num_mapper = dict()

# Processing mapped numbers
for _ in range(int(nums)):
    num, char = input().strip().split()
    num_mapper[num] = char

# Processing queries
for _ in range(int(queries)):
    num = input().strip()
    result = num_mapper.get(num, UNKNOWN_KEY_MESSAGE)
    print(result)
