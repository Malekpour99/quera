# https://quera.org/problemset/275458
# -----------------------------------

HORSE_BITE_LENGTH = 3  # inch

number_of_pieces = int(input().strip())
pieces = list(map(int, input().strip().split()))

print(sum(pieces) + (number_of_pieces - 1) * HORSE_BITE_LENGTH)
