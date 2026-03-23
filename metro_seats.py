# https://quera.org/problemset/218361
# -----------------------------------

first_row = list(map(int, input().strip().split()))
second_row = list(map(int, input().strip().split()))

eye_to_eye_count = 0

for i in range(len(first_row)):
    if first_row[i] == 1 and second_row[i] == 1:
        eye_to_eye_count += 1

print(eye_to_eye_count)
