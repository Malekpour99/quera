n = int(input().strip())
seq = sorted(list(map(int, input().strip().split())))

if n % 2 == 0:
    target_num = seq[n // 2 - 1]
else:
    target_num = seq[n // 2]

cost = 0
for num in seq:
    cost += abs(num - target_num)

print(f"{target_num} {cost}")
