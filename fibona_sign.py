# https://quera.org/problemset/17675
# ----------------------------------

n = int(input().strip())

previous_fib_member: int = 1
next_fib_member: int = 1
sign_string: str = ""

for i in range(1, n + 1):
    if i == next_fib_member:
        sign_string += "+"
        previous_fib_member, next_fib_member = (
            next_fib_member,
            previous_fib_member + next_fib_member,
        )
    else:
        sign_string += "-"

print(sign_string)
