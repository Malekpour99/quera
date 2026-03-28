# https://quera.org/problemset/7609
# ---------------------------------

from collections import Counter
from typing import Final

BAD_LETTER: Final = "bad"
GOOD_LETTER: Final = "khoob"

text = input().strip()

counted_characters: dict[str, int] = Counter(text)

is_bad = False

for count_ in counted_characters.values():
    if count_ % 2 != 0:
        is_bad = True
        break

if is_bad:
    print(BAD_LETTER)
else:
    print(GOOD_LETTER)
