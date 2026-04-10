# https://quera.org/problemset/64434
# ----------------------------------

height, width = map(int, input().strip().split())

for i in range(3):
    x_string = "X" * width
    dot_string = "." * width

    if i % 2 == 0:
        row_string = x_string + dot_string + x_string
    else:
        row_string = dot_string + x_string + dot_string

    for _ in range(height):
        print(row_string)
