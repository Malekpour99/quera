# https://quera.org/problemset/3430?tab=description
# -------------------------------------------------

word = input().strip()

word_characters = list(word)

for i, ch in enumerate(word_characters):
    for j in range(0, i):
        word_characters[j] = ch

    print("".join(word_characters))
