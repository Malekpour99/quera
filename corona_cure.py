# https://quera.org/problemset/178600
# -----------------------------------

shekarestan_contaminated = int(input().strip())
shekarestan_deaths = int(input().strip())
shekarestan_effectiveness = shekarestan_contaminated - shekarestan_deaths

namakestan_contaminated = int(input().strip())
namakestan_deaths = int(input().strip())
namakestan_effectiveness = namakestan_contaminated - namakestan_deaths


if shekarestan_effectiveness > namakestan_effectiveness:
    print("Shekarestan")
elif namakestan_effectiveness > shekarestan_effectiveness:
    print("Namakestan")
else:
    print("Equal")
