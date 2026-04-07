# https://quera.org/problemset/170060
# -----------------------------------

people_count, acceptable_height_difference = map(int, input().strip().split())
people_heights = list(map(int, input().strip().split()))

height_to_reach = max(people_heights) - acceptable_height_difference

required_boxes: int = 0

for height in people_heights:
    required_boxes += max(0, height_to_reach - height)

print(required_boxes)
