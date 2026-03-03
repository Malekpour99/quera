# https://quera.org/problemset/129726
# -----------------------------------


def separator(ls) -> tuple[list, list]:
    evens, odds = [], []
    for num in ls:
        (evens if num % 2 == 0 else odds).append(num)

    return evens, odds
