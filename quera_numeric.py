# https://quera.org/problemset/306545?tab=description
# ---------------------------------------------------
def queranumeric(order: list[str], words: list[str]) -> list[str]:
    # Create a mapping from character to its priority/index
    char_order = {char: idx for idx, char in enumerate(order)}

    # Define a key function for sorting
    def sort_key(word):
        # Convert each character to its priority
        # Characters not in order get a high value (sort last)
        return [char_order.get(char, float('inf')) for char in word]

    # Sort the words using the custom key
    return sorted(words, key=sort_key)
