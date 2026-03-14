# https://quera.org/problemset/41175
# ----------------------------------

gunnar_dice = list(map(int, input().strip().split()))
emma_dice = list(map(int, input().strip().split()))

# calculated total mean for each person's dice (works since dice are monotonic with equal chance)
# otherwise calculation of mean based on a distributed change and values were required
gunnar_chance = sum(gunnar_dice)
emma_chance = sum(emma_dice)

if gunnar_chance > emma_chance:
    print("Gunnar")
elif gunnar_chance < emma_chance:
    print("Emma")
else:
    print("Tie")
