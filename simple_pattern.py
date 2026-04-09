# https://quera.org/problemset/140037
# -----------------------------------

n = int(input().strip())

sequence: str = ""
num: int = 1

while len(sequence) < n:
    sequence += str(num)
    num += 1

print(sequence[n - 1])
