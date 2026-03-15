# https://quera.org/problemset/252330
# -----------------------------------

from collections import Counter

classes = int(input().strip())

all_classes: list[list[str]] = []  # list of favorite words for each class

for _ in range(classes):
    class_favorite_words: list[str] = []
    students = int(input().strip())
    for _ in range(students):
        class_favorite_words.append(input().strip())

    all_classes.append(class_favorite_words)

for class_ in all_classes:
    total_characters: dict[str, int] = {}
    for fav_word in class_:
        character_count = Counter(fav_word)
        for ch, count in character_count.items():
            total_character_count = total_characters.get(ch, 0)
            if total_character_count < count:
                total_characters[ch] = count

    print(sum(total_characters.values()))
