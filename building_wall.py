# https://quera.org/problemset/179662
# -----------------------------------

wall_length, brick_length = map(int, input().strip().split())

print(wall_length % brick_length)
