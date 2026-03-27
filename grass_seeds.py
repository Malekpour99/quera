# https://quera.org/problemset/281769
# -----------------------------------

placeholders_count, seeds_count = map(int, input().strip().split())

#  These empty slots can create at most (n−k)+1 separate groups of seeds.
#  If k is greater than the number of groups, the excess seeds must form adjacent pairs.
#  Formula: max(0,k−((n−k)+1))=max(0,2k−n−1).
adjacent_seeds_count: int = max(0, 2 * seeds_count - placeholders_count - 1)

print(adjacent_seeds_count)
