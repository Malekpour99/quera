# https://quera.org/problemset/2886
# ---------------------------------

h, m = map(int, input().strip().split())

mirrored_hour = (12 - h) % 12
mirrored_minute = (60 - m) % 60

print(f"{mirrored_hour:02d}:{mirrored_minute:02d}")
