# https://quera.org/problemset/209098
# -----------------------------------

cases = int(input().strip())

for _ in range(cases):

    columns_count, subtraction_cap = map(int, input().strip().split())
    columns = list(map(int, input().strip().split()))

    # ops[i] stores the number of operations starting at index i
    ops = [0] * columns_count
    current_subtraction: int = 0
    is_cake: bool = True

    for i in range(columns_count):
        # If an operation started at i-k, it no longer affects index i
        # Because the operation covers range [start, start + k - 1]
        # So at index i, an operation starting at i-k covers up to i-1
        if i >= subtraction_cap:
            current_subtraction -= ops[i - subtraction_cap]

        # Calculate the remaining layers at current column after previous operations
        remaining = columns[i] - current_subtraction

        if remaining < 0:
            # We subtracted more than available layers
            is_cake = False
            break

        if remaining > 0:
            # We need to start 'remaining' operations at index i to clear this column
            # But we can only do this if there is enough space (k columns) remaining
            if i + subtraction_cap > columns_count:
                is_cake = False
                break

            ops[i] = remaining
            current_subtraction += remaining

    if is_cake:
        print("Cake")
    else:
        print("Fake")
