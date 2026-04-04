# https://quera.org/problemset/177665
# -----------------------------------

str_len = int(input().strip())
text_string = input().strip()

i: int = 0

while i < str_len - 1:
    if text_string[i] == text_string[i + 1]:
        text_string = text_string[:i] + text_string[i + 2 :]
        str_len -= 2
        i = max(0, i - 1)
    else:
        i += 1

print(text_string)
