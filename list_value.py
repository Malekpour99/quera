# https://quera.org/problemset/76278
# ----------------------------------


def calculator(n, m, li):
    list_value = 0
    counter = m
    to_add = True
    for num in li:
        list_value += num if to_add else -num
        counter -= 1
        if counter == 0:
            counter = m
            to_add = not to_add

    return list_value
