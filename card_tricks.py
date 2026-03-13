# https://quera.org/problemset/175188
# -----------------------------------

days = int(input().strip())
decks = [input().strip() for _ in range(days)]

for deck in decks:
    trick_moves = 0
    is_last_seen_card_down = False
    for card in deck:
        if card == "0":
            if not is_last_seen_card_down:
                is_last_seen_card_down = True
                trick_moves += 1
        # update last seen card state only when current card state changes
        elif is_last_seen_card_down:
            is_last_seen_card_down = False

    print(trick_moves)
