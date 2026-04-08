# https://quera.org/problemset/176778
# -----------------------------------

animals_count, blanket_length = map(int, input().strip().split())
animals = sorted(list(map(int, input().strip().split())))

i: int = 0
blanket_count: int = 0

while i < animals_count:
    coverage = animals[i] + blanket_length
    while i + 1 < animals_count and animals[i + 1] <= coverage:
        i += 1

    blanket_count += 1
    i += 1

print(blanket_count)
