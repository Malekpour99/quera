# https://quera.org/problemset/72881
# ----------------------------------

pots, required_vegetable_per_pot, vegetable_inventory = map(
    float, input().strip().split()
)

if pots * required_vegetable_per_pot <= vegetable_inventory:
    print("Kafie!")
else:
    print("Na! yeki bayad bere sabzi bekhare")
