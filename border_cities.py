# https://quera.org/problemset/228669
# -----------------------------------

rows = int(input().strip())
columns = int(input().strip())

if rows < 2 or columns < 2:
    print(rows * columns)  # Every house is considered a border city
else:
    print(
        (rows + columns) * 2 - 4
    )  # deducting duplicated corner cities from calculated perimeter
