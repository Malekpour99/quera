# https://quera.org/problemset/108665
# -----------------------------------

from typing import Final

VOWELS: Final = {"a", "e", "i", "o", "u"}

word = input().strip()

vowel_count = 0
for ch in word:
    if ch in VOWELS:
        vowel_count += 1

print(2**vowel_count)
