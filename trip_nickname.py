# https://quera.org/problemset/209104
# -----------------------------------

from typing import Final

HAS_TRAVELED: Final = "Y"
HAS_NOT_TRAVELED: Final = "N"

HAJI_NICKNAME: Final = "Haji"
KARBALAEE_NICKNAME: Final = "Karbalaee"
MASHTI_NICKNAME: Final = "Mashti"
AGHA_NICKNAME: Final = "Agha"

trip_nickname_mapper: dict[int, str] = {
    0: HAJI_NICKNAME,
    1: KARBALAEE_NICKNAME,
    2: MASHTI_NICKNAME,
}

nickname: str = AGHA_NICKNAME

trips = input().strip()

for i, status in enumerate(trips):
    if status == HAS_TRAVELED:
        nickname = trip_nickname_mapper.get(i, nickname)
        break

print(nickname)
