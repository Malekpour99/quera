import heapq

n, k = map(int, input().strip().split())
costs = list(map(int, input().strip().split()))


pq = costs[:]
heapq.heapify(pq)

min_total_cost = float("inf")
min_char_cost = min(costs)

while True:
    smallest_n = heapq.nsmallest(n, pq)
    current_sum = sum(smallest_n)

    if current_sum < min_total_cost:
        min_total_cost = current_sum
    else:
        if len(pq) >= n:
            break

    if len(pq) >= n:
        threshold = smallest_n[-1]
        min_heap_val = pq[0]

        if min_heap_val + min_char_cost >= threshold:
            break

    c = heapq.heappop(pq)
    for w in costs:
        heapq.heappush(pq, c + w)

print(min_total_cost)
