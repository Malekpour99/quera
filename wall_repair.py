# https://quera.org/problemset/6580?tab=description
# -------------------------------------------------

top_left_x, top_left_y = map(int, input().strip().split())
side_length = int(input().strip())
glass_x, glass_y = map(int, input().strip().split())

if (top_left_x <= glass_x <= top_left_x + side_length) and (
    top_left_y - side_length <= glass_y <= top_left_y
):
    print("Mahdi")
else:
    print("Parsa")
