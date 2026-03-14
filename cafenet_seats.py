# https://quera.org/problemset/220668
# -----------------------------------

computers, groups = map(int, input().strip().split())
cafe_net = [0] * computers
for _ in range(groups):
    index, members = map(int, input().strip().split())
    for i in range(index - 1, computers):
        if cafe_net[i: i + members] == [0] * members:
            for j in range(members):
                cafe_net[i + j] = 1
            break

    print("".join(str(pc) for pc in cafe_net))
