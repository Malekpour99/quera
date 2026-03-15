def count_smaller_numbers(num_list: list[int], number: int) -> int:
    """
    Count smaller numbers in the input array compared to the input number
    """
    count = 0
    for num in num_list:
        if num < number:
            count += 1

    return count


_, questions = map(int, input().strip().split())
num_list = list(map(int, input().strip().split()))
for _ in range(questions):
    query_number = int(input().strip())
    print(count_smaller_numbers(num_list, query_number))
