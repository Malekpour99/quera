# https://quera.org/problemset/140033
# -----------------------------------

from typing import Final

vowels: Final = {"a", "e", "i", "o", "u"}

word = input().strip()

vowel_count = 0
for ch in word:
    if ch in vowels:
        vowel_count += 1

print(vowel_count)
