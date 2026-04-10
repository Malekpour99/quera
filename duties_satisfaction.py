# https://quera.org/problemset/275475
# -----------------------------------

total_duties, zahra_cap = map(int, input().strip().split())

# tuple[int, int]: (zahra-satisfaction, others-satisfaction)
satisfaction_factors: list[tuple[int, int]] = []

for _ in range(total_duties):
    zahra_sat, oth_sat = map(int, input().strip().split())
    satisfaction_factors.append((zahra_sat, oth_sat))

# considering satisfaction difference for gaining maximum satisfaction
satisfaction_factors.sort(key=lambda s: s[0] - s[1], reverse=True)

total_satisfaction: int = 0

for i, satisfaction_values in enumerate(satisfaction_factors):
    if i < zahra_cap:
        total_satisfaction += satisfaction_values[0]
    else:
        total_satisfaction += satisfaction_values[1]

print(total_satisfaction)
