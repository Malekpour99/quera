# https://quera.org/problemset/26651?tab=description
# --------------------------------------------------

questions = int(input().strip())
breathe_take_counts = list(map(int, input().strip().split()))
problem_solver_counts = list(map(int, input().strip().split()))

total_breathe_takes = 0
for i in range(questions):
    total_breathe_takes += breathe_take_counts[i] * problem_solver_counts[i]

print(total_breathe_takes)
