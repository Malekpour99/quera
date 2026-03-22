# https://quera.org/problemset/28948
# ----------------------------------

raw_str = input().strip()

characters: list[str] = []

for ch in raw_str:
    if ch != "=":
        characters.append(ch)
    elif ch == "=" and len(characters):
        characters.pop()


print("".join(characters))
