# https://quera.org/problemset/2659
# ---------------------------------

n = int(input().strip())
original_pattern = input().strip()
user_input = input().strip()

mismatch_count: int = 0

for i in range(n):
    if original_pattern[i] != user_input[i]:
        mismatch_count += 1

print(mismatch_count)
