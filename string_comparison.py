# https://quera.org/problemset/102248
# -----------------------------------


def compare(string1, string2):
    while string1 and string2:
        if string1[0] < string2[0]:
            string1 = string1[1:]
        elif string1[0] == string2[0]:
            string1 = string1[1:]
            string2 = string2[1:]
        else:
            string2 = string2[1:]

        if string1 and string2:
            string1 = string1[::-1]
            string2 = string2[::-1]

    if string1 or string2:
        return string1 if string1 else string2
    else:
        return "Both strings are empty!"
