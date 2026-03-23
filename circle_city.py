# https://quera.org/problemset/218362
# -----------------------------------

# Process the n radial street directions
# We only need to check if there is at least one '0' and one '1'

# The m circular street directions are read implicitly by the input reading
# but do not need to be processed for the logic.
# Circular streets always form a cycle, ensuring connectivity between
# radial streets on the same layer.

n, m = map(int, input().strip().split())
radial_streets = list(input().strip().split())
circular_streets = list(input().strip().split())

has_outward = True if "1" in radial_streets else False
has_inward = True if "0" in radial_streets else False

if has_outward and has_inward:
    print("YES")
else:
    print("NO")
