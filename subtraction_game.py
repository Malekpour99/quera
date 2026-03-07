# https://quera.org/problemset/87176
# ----------------------------------


def game(number):
    if not 9 < number < 100:
        raise Exception("Input number must be between 10 and 99")

    # number_string = str(number)
    # return abs(int(number_string[0]) - int(number_string[1]))

    return abs(number // 10 - number % 10)
