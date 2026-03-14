processed_queries: dict[int, int] = {}
num_count: dict[int, int] = {}


_, queries_count = map(int, input().strip().split())
num_list = list(map(int, input().strip().split()))

for num in num_list:
    num_count[num] = num_count.get(num, 0) + 1

queries = list(int(input().strip()) for _ in range(queries_count))

for i in range(1, max(queries) + 1):
    processed_queries[i] = processed_queries.get(i - 1, 0) + num_count.get(i, 0)

for query in queries:
    print(processed_queries.get(query - 1, 0))
