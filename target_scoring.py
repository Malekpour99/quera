# https://quera.org/problemset/141570
# -----------------------------------

OUT_OF_ZONE_MESSAGE = "out"
WHITE_ZONE_MESSAGE = "white"
BLACK_ZONE_MESSAGE = "black"

hit_point = int(input().strip())

if hit_point < 1:
    print(OUT_OF_ZONE_MESSAGE)
elif hit_point < 7:
    print(WHITE_ZONE_MESSAGE)
else:
    print(BLACK_ZONE_MESSAGE)
