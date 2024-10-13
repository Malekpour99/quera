rows = int(input())
painted_zone = [list(map(int, input().split())) for _ in range(rows)]

total_perimeter = 0
if not painted_zone:
    print(total_perimeter)
    exit(0)
    
height = 1
previous_start, previous_end = None, None

for zone in painted_zone:
    total_perimeter += (zone[1] - zone[0] + height) * 2
    if previous_start is not None and previous_end is not None:
        start_diff = max(previous_start, zone[0])
        end_diff = min(previous_end, zone[1])
        if end_diff - start_diff > 0:
            total_perimeter -= (end_diff - start_diff) * 2
        
    previous_start, previous_end = zone

print(total_perimeter)
