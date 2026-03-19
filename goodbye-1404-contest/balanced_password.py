n = int(input().strip())
for _ in range(n):
    d1, d2, d3, d4, d5, d6 = map(int, input().strip().split())
    if d1 + d2 + d3 == d4 + d5 + d6:
        print("Possible")
    else:
        print("Impossible")
