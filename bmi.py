# https://quera.org/problemset/3404
# ---------------------------------


def calculate_bmi(*, weight: int, height: float) -> float:
    return weight / (height * height)


def get_bmi_description(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


weight_kg = int(input().strip())
height_meter = float(input().strip())

bmi = calculate_bmi(weight=weight_kg, height=height_meter)
bmi_description = get_bmi_description(bmi)

print(f"{bmi:.2f}")
print(bmi_description)
