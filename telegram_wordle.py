# https://quera.org/problemset/254220?tab=description
# ---------------------------------------------------
from collections import Counter

# Game Status Flag
has_guessed = False

# Game Messages
GAME_OVER_MESSAGE = "Game Over"
INVALID_LENGTH_MESSAGE = "Invalid Length"
CORRECT_GUESS_MESSAGE = "G"
SEMI_GUESS_MESSAGE = "Y"
WRONG_GUESS_MESSAGE = "R"

# Processing user input considering below structure:
# :param 1 -> keyword to be guessed
# :param 2 -> number of user guesses
# :param > 2 -> user guesses
keyword = input().strip()
keyword_length = len(keyword)
number_of_guesses = int(input())
user_guesses = [input().strip() for _ in range(number_of_guesses)]

# Playing Wordle Game
for guess in user_guesses:
    guess_result = [""] * keyword_length
    keyword_character_count = Counter(keyword)
    if has_guessed:
        print(GAME_OVER_MESSAGE)
    elif len(guess) != keyword_length:
        print(INVALID_LENGTH_MESSAGE)
    else:
        for i, ch in enumerate(guess):
            # Correct Guess
            if ch == keyword[i]:
                guess_result[i] = CORRECT_GUESS_MESSAGE
                keyword_character_count[ch] -= 1
        for i, ch in enumerate(guess):
            if guess_result[i] == "":
                # Semi Guess (correct character, wrong position)
                if keyword_character_count.get(ch):
                    guess_result[i] = SEMI_GUESS_MESSAGE
                    keyword_character_count[ch] -= 1
                # Wrong Guess
                else:
                    guess_result[i] = WRONG_GUESS_MESSAGE

        result_str = "".join(guess_result)

        if result_str == CORRECT_GUESS_MESSAGE * keyword_length:
            has_guessed = True

        print(result_str)
