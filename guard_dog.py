# https://quera.org/problemset/271650
# -----------------------------------


def check_escape_possibility(n: int, m: int, x: int, y: int, s: int) -> None:
    """
    center of this coordinates is (1, 1) placed at the top-left corner

    (n, m): destination coordinates
    (x, y): dog house coordinates
    s: maximum guarding distance covered by dog
    """

    if (
        (max(1, x - s) == 1 and max(1, y - s) == 1)  # left and top are closed
        or (min(n, x + s) == n and min(m, y + s) == m)  # bottom and right are closed
        or (max(1, x - s) == 1 and min(n, x + s) == n)  # top and bottom are closed
        or (max(1, y - s) == 1 and min(m, y + s) == m)  # left and right are closed
    ):
        print("NO")
    else:
        print("YES")


t = int(input().strip())

for _ in range(t):
    n, m, x, y, s = map(int, input().strip().split())
    check_escape_possibility(n, m, x, y, s)
