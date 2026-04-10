# https://quera.org/problemset/3431
# ---------------------------------


rows, columns = map(int, input().strip().split())
grid: list[str] = []
for _ in range(rows):
    grid.append(input().strip())

target_word = input().strip()

count: int = 0
word_len: int = len(target_word)

# 1. Horizontal Search (Left to Right)
for row in range(rows):
    for col in range(columns - word_len + 1):
        if grid[row][col : col + word_len] == target_word:
            count += 1

# 2. Vertical Search (Top to Bottom)
if rows >= word_len:
    for col in range(columns):
        for row in range(rows - word_len + 1):
            vertical_sub = "".join(grid[row + i][col] for i in range(word_len))

            if vertical_sub == target_word:
                count += 1

print(count)
