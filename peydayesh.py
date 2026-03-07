# https://quera.org/problemset/102250
# -----------------------------------

GUESS_OPTIONS = {1, 2, 3, 4}


def find(num1, num2, num3):
    return GUESS_OPTIONS.difference({num1, num2, num3}).pop()
