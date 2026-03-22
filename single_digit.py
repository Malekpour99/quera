# https://quera.org/problemset/3539
# ---------------------------------

number = input().strip()

temp_sum = 0

while len(number) > 1:
    for d in number:
        temp_sum += int(d)

    number, temp_sum = str(temp_sum), 0

print(number)
