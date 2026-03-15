n, k = map(int, input().split())
seq = list(map(int, input().split()))

seq_2 = sorted([seq[i] - i * k for i in range(n)])

target_num = seq_2[n // 2 - 1] if n % 2 == 0 else seq_2[n // 2]

cost = 0
for num in seq_2:
    cost += abs(num - target_num)

print(cost)
