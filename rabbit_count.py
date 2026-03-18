# https://quera.org/problemset/157645
# -----------------------------------

rabbits, rabbits_hunted_by_fox = map(int, input().strip().split())
year = int(input().strip())

for _ in range(year):
    rabbits = rabbits * 2 - rabbits_hunted_by_fox

print(rabbits)
