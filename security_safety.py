# https://quera.org/problemset/33036
# ----------------------------------

import re
from collections import defaultdict


class Security:
    def secure(self, info: str) -> str:
        info_data: list[str] = info.split()
        for i, data in enumerate(info_data):
            if self.is_social_account_info(data):
                web_address, account_name = data.split("/")
                encrypted_account = self.encrypt(account_name)

                info_data[i] = web_address + "/" + encrypted_account

        return " ".join(info_data)

    def is_social_account_info(self, param: str) -> bool:
        # Regular Expression Pattern for [Social Network Name]:www.[domain]/[Account Name]
        # ^                   : Start of string
        # [A-Z]               : Network name starts with uppercase English letter
        # [a-zA-Z0-9]*        : Rest of network name (alphanumeric)
        # :                   : Literal colon separator
        # www\.               : Literal 'www.'
        # [a-z0-9.]+          : Domain (lowercase letters, numbers, dots)
        # /                   : Literal slash separator
        # [a-zA-Z0-9_]+       : Account name (letters, numbers, underscores)
        # $                   : End of string
        pattern = r"^[A-Z][a-zA-Z0-9]*:www\.[a-z0-9.]+/[a-zA-Z0-9_]+$"

        if re.fullmatch(pattern, param):
            return True

        return False

    def encrypt(self, s: str) -> str:
        string_encrypted_value: str = ""
        character_counter: dict[str, int] = defaultdict(int)
        for ch in s:
            ch_value = (ord(ch) - 96) * (character_counter.get(ch, 0) + 1)
            character_counter[ch] += 1
            string_encrypted_value += str(ch_value)

        return string_encrypted_value
