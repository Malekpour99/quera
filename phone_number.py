# https://quera.org/problemset/291610
# -----------------------------------

import re
from typing import Final

INVALID_NUMBER_MESSAGE: Final = "invalid"

n = int(input().strip())

sanitized_phone_numbers: list[str] = []

pattern_09 = r"^09(\d{9})$"
pattern_98 = r"^98(\d{10})$"
pattern_plus98 = r"^\+98(\d{10})$"

for _ in range(n):
    phone_number = input().strip()

    if phone_number.startswith("+98"):
        match = re.match(pattern_plus98, phone_number)
    elif phone_number.startswith("98"):
        match = re.match(pattern_98, phone_number)
    elif phone_number.startswith("09"):
        match = re.match(pattern_09, phone_number)
    else:
        match = None

    if match:
        digits = match.group(1)
        if len(digits) == 9:
            sanitized_phone_numbers.append(f"+989{digits}")
        else:
            sanitized_phone_numbers.append(f"+98{digits}")
    else:
        sanitized_phone_numbers.append(INVALID_NUMBER_MESSAGE)

print(*sanitized_phone_numbers, sep="\n")
