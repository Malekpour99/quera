# https://quera.org/problemset/254219
# -----------------------------------

college_account = list(map(int, input().strip().split()))
boot_camp_account = list(map(int, input().strip().split()))
contest_account = list(map(int, input().strip().split()))

debt_matrix = [
    college_account,
    boot_camp_account,
    contest_account,
]

# Calculate net position for each company
n = len(debt_matrix)
net_position = [0] * n

for i in range(n):
    for j in range(n):
        if i != j:
            net_position[i] += debt_matrix[j][i]  # money owed TO i
            net_position[i] -= debt_matrix[i][j]  # money owed BY i

# Create new simplified debt matrix
new_debt_matrix = [[0] * n for _ in range(n)]

# Simple pairing algorithm (greedy approach)
creditors = []
debtors = []

for i in range(n):
    if net_position[i] > 0:
        creditors.append((i, net_position[i]))  # (company_index, amount_owed_to_them)
    elif net_position[i] < 0:
        debtors.append((i, -net_position[i]))  # (company_index, amount_they_owe)

# Match debtors to creditors
creditor_idx = 0
debtor_idx = 0

while creditor_idx < len(creditors) and debtor_idx < len(debtors):
    creditor_company, creditor_amount = creditors[creditor_idx]
    debtor_company, debtor_amount = debtors[debtor_idx]

    # Determine payment amount
    payment = min(creditor_amount, debtor_amount)

    if payment > 0:
        new_debt_matrix[debtor_company][creditor_company] = payment

    # Update amounts
    creditors[creditor_idx] = (creditor_company, creditor_amount - payment)
    debtors[debtor_idx] = (debtor_company, debtor_amount - payment)

    if creditors[creditor_idx][1] == 0:
        creditor_idx += 1
    if debtors[debtor_idx][1] == 0:
        debtor_idx += 1

# Print result
for company in new_debt_matrix:
    print(" ".join(str(num) for num in company))
