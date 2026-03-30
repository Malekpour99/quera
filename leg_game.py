# https://quera.org/problemset/69899
# ----------------------------------

n, k = map(int, input().strip().split())

index: int = 0  # Starting index of legs for game
remaining_legs = n * 2
legs: list[int] = []

for i in range(1, n + 1):
    legs.extend([i, i])

while remaining_legs > 1:
    for _ in range(k - 1):
        print(legs[index], end=" ")
        index = (index + 1) % remaining_legs

    print(legs[index])
    legs.pop(index)
    remaining_legs -= 1
    index %= remaining_legs

    if remaining_legs == 2 and legs[0] == legs[1]:
        break

print(f"winner:{legs[0]}")
