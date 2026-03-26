# https://quera.org/problemset/82378
# ----------------------------------

from typing import Final

RATION_PETROL_COST: Final = 1500
FREE_PETROL_COST: Final = 3000

required_petrol = int(input().strip())
remaining_ration = int(input().strip()) + 60

if required_petrol > remaining_ration:
    petrol_cost = (
        remaining_ration * RATION_PETROL_COST
        + (required_petrol - remaining_ration) * FREE_PETROL_COST
    )
else:
    petrol_cost = required_petrol * RATION_PETROL_COST

print(petrol_cost)
