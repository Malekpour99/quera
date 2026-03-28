# https://quera.org/problemset/316820
# -----------------------------------

n = int(input().strip())
weights = sorted(map(int, input().strip().split()), reverse=True)
target = input().strip()

romina_team: list[int] = []
ali_team: list[int] = []

for i in range(n):
    if i == 0:
        # First pick belongs to Romina
        romina_team.append(weights[i])
    else:
        # Subsequent picks are in blocks of 2
        # Group 0 (indices 1, 2) -> Ali
        # Group 1 (indices 3, 4) -> Romina
        # Group 2 (indices 5, 6) -> Ali
        group_idx = (i - 1) // 2

        if group_idx % 2 == 0:
            ali_team.append(weights[i])
        else:
            romina_team.append(weights[i])

sum_romina = sum(romina_team)
sum_ali = sum(ali_team)

if target == "romina":
    my_sum = sum_romina
    opp_team = ali_team
else:
    my_sum = sum_ali
    opp_team = romina_team

sum_opp = sum(opp_team)

diff = sum_opp - my_sum

if diff < 0:
    # Already winning without bribes
    print(0)
else:
    # Need to bribe opponents to reduce their sum by more than 'diff'
    bribed_weights = []
    current_bribe_sum = 0

    for w in opp_team:
        current_bribe_sum += w
        bribed_weights.append(w)
        # Check if condition is met: removed weight > diff
        if current_bribe_sum > diff:
            break

    print(len(bribed_weights))
    print(*(bribed_weights))
