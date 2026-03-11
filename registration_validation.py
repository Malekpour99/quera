# https://quera.org/problemset/21205
# ----------------------------------

import re
from typing import Final

RESERVED_USERNAMES: Final = {"codecup", "quera"}


def check_registration_rules(**kwargs) -> list[str]:
    valid_users: list[str] = []
    for username, password in kwargs.items():
        if (
            username in RESERVED_USERNAMES
            or len(username) < 4
            or len(password) < 6
            or re.fullmatch(
                r"^[0-9]+$", password
            )  # password.isdigit() can be used as well
        ):
            continue

        valid_users.append(username)

    return valid_users
