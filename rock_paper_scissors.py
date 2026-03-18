# https://quera.org/problemset/18213
# ----------------------------------

# P, R, S: Shangdbao's counts for Paper, Rock, Scissors
# a, b, c: Friend's counts for Paper, Rock, Scissors
(
    P,
    R,
    S,
    friend_paper_action,
    friend_rock_action,
    friend_scissors_action,
) = map(int, input().strip().split())

# --- Maximize Wins ---
wins_vs_P = min(P, friend_scissors_action)
wins_vs_R = min(R, friend_paper_action)
wins_vs_S = min(S, friend_rock_action)

total_wins = wins_vs_P + wins_vs_R + wins_vs_S

# --- Update Remaining Counts ---
rem_P = P - wins_vs_P
rem_R = R - wins_vs_R
rem_S = S - wins_vs_S
rem_p_action = friend_paper_action - wins_vs_R
rem_r_action = friend_rock_action - wins_vs_S
rem_c_action = friend_scissors_action - wins_vs_P

# --- Maximize Draws ---
draws_vs_P = min(rem_P, rem_p_action)
draws_vs_R = min(rem_R, rem_r_action)
draws_vs_S = min(rem_S, rem_c_action)

total_draws = draws_vs_P + draws_vs_R + draws_vs_S

# --- Losses and Score ---
total_games = P + R + S
total_losses = total_games - total_wins - total_draws

# Score calculation: Win (+1), Loss (-1), Draw (0)
score = total_wins - total_losses

print(score)
