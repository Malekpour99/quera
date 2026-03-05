# https://quera.org/problemset/316831
# -----------------------------------

fibonacci_memo: dict[int, int] = {}


def fib(n: int, memo: dict[int, int] = fibonacci_memo) -> int:
    """
    Calculates n-th fibonacci sequence member using an efficient
    way which utilizes a memory map for previously calculated values
    """
    if n < 1:
        return 0

    if n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        result = fib(n - 1, memo) + fib(n - 2, memo)
        memo[n] = result
        return result


def calculate_name_hash(name: str) -> int:
    hash_value = 0
    for i, ch in enumerate(name):
        hash_value += ord(ch) * fib(i + 1)

    return hash_value


def assign_tables(
    groups: dict[str, list[str]],
    tables_num: int,
) -> tuple[dict[str, int], list[tuple[str, int, str]]]:
    group_tables: dict[str, int] = {}
    assigned_tables: dict[int, list[str]] = {}
    collisions: list[tuple[str, int, str]] = []

    for group, members in groups.items():
        # Calculating group table
        group_hash = 0
        for member in members:
            group_hash += calculate_name_hash(member)
        table = (group_hash * len(members)) % tables_num

        # Dedicating table to group
        group_tables[group] = table

        # Check for collisions and update previous records
        if previous_groups := assigned_tables.get(table):
            collisions.append((group, table, previous_groups[-1]))
            previous_groups.append(group)
        else:
            assigned_tables[table] = [group]

    return group_tables, collisions
