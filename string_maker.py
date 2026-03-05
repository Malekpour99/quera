# https://quera.org/problemset/9110?tab=description
# -------------------------------------------------

left, right = map(int, input().strip().split())

string = "10"

trans = str.maketrans("01", "10")

while len(string) < right:
    string += string.translate(trans)

    # solution without using translation table:
    # string = string + ''.join('1' if bit == '0' else '0' for bit in string)


print(string[left - 1 : right])
