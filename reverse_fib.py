# https://quera.org/problemset/303
# --------------------------------


def show_fib_nth(*, num: int, next_num: int) -> None:
    """
    print fibonacci sequence in reverse order
    where num is the n-th member and
    next_num is the n+1-th member
    """

    print(num)
    if next_num - num == 0:
        return
    else:
        show_fib_nth(num=(next_num - num), next_num=num)


num = int(input().strip())
next_num = int(input().strip())

show_fib_nth(num=num, next_num=next_num)
