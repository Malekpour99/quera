# https://quera.org/problemset/33034
# ----------------------------------


def coloring(ls):
    n = len(ls)  # layers
    r = len(ls[0])  # rows in each layer
    c = len(ls[0][0])  # columns in each row

    for i in range(n):
        for j in range(r):
            for k in range(c):
                if i == 0 or i == n - 1 or j == 0 or j == r - 1 or k == 0 or k == c - 1:
                    ls[i][j][k] = 1
                else:
                    ls[i][j][k] = 0
