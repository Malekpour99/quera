# https://quera.org/problemset/129728?tab=description
# ---------------------------------------------------
print(" ".join(sorted([ch if (ord(ch) - 97) % 2 == 0 else ch.upper() for ch in str(input())], reverse=True)))
