# https://quera.org/problemset/9109
# ---------------------------------

from collections import Counter

total_count = int(input().strip())
markers_count: dict[int, int] = Counter(map(int, input().strip().split()))

min_count: int = total_count
min_marker_color: int | float = float("inf")

for color, count in markers_count.items():
    if count < min_count:
        min_count, min_marker_color = count, color
    elif count == min_count and color < min_marker_color:
        min_count, min_marker_color = count, color

print(min_marker_color)
