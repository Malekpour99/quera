# https://quera.org/problemset/140027
# -----------------------------------

from typing import Final

# 0-indexed
TEXT: Final = "quera is the best platform.‍‍"

n = int(input().strip())

print(ord(TEXT[n - 1]))
