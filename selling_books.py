# https://quera.org/problemset/9596
# ---------------------------------

from typing import Final

REMAIN: Final = "YES"
NO_REMAIN: Final = "NO"

book1, book2, book3 = map(int, input().strip().split())

# Calculate parities - parity must be (1, 0, 0) or (0, 1, 1) for each book to remain
parities = (book1 % 2, book2 % 2, book3 % 2)

ans: list[str] = []

# Check possibility for Type 1
if parities == (1, 0, 0) or parities == (0, 1, 1):
    ans.append(REMAIN)
else:
    ans.append(NO_REMAIN)

# Check possibility for Type 2
if parities == (0, 1, 0) or parities == (1, 0, 1):
    ans.append(REMAIN)
else:
    ans.append(NO_REMAIN)

# Check possibility for Type 3
if parities == (0, 0, 1) or parities == (1, 1, 0):
    ans.append(REMAIN)
else:
    ans.append(NO_REMAIN)

print(" ".join(ans))
