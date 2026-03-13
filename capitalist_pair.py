# https://quera.org/problemset/8358
# ---------------------------------

n = int(input().strip())
capitalists = list(map(int, input().strip().split()))

negative_capitalists: list[int] = []
for capitalist in capitalists:
    if capitalist < 0:
        negative_capitalists.append(capitalist)

# for each negative capitalist a (a, b) pair can be created where a + b < a - b
print((n - 1) * len(negative_capitalists))
