# https://quera.org/problemset/66864
# ----------------------------------

sequence = "".join(str(n) for n in range(1, 5001))

index = int(input().strip())

print(sequence[index - 1])
