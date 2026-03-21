# https://quera.org/problemset/235327
# -----------------------------------

t = int(input().strip())

for _ in range(t):
    jump, fall, height = map(int, input().strip().split())

    day_count = 0
    current_height = 0

    while current_height < height:
        day_count += 1
        current_height += jump
        if current_height >= height:
            break
        else:
            current_height -= fall

    print(day_count)
