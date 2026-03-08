# https://quera.org/problemset/87183
# ----------------------------------

import os
from collections import defaultdict

NORMAL_WIN_MESSAGE = "Win! Normally!"
CHEAT_WIN_MESSAGE = "Win! you can win if you cheat on '{file_name}'!"
LOSE_MESSAGE = "Lose! you can't win this game!"


def combet(SAliB_format: str, Sajjad_format: str, path: str) -> str:
    file_name_cheat_value: dict[str, int] = defaultdict(int)
    SAliB_format_count = 0
    Sajjad_format_count = 0

    for _, _, files in os.walk(path):
        for file in files:
            _, ext = os.path.splitext(file)
            file_format = ext.lstrip(".")
            file_name = os.path.splitext(file)[0]
            if file_format == Sajjad_format:
                Sajjad_format_count += 1
                # prevent over-calculating file_names with matched format for cheating
                file_name_cheat_value[file_name] -= 1
            elif file_format == SAliB_format:
                SAliB_format_count += 1
                # changing these file names will reduce salib matches and also increase sajjad matches
                file_name_cheat_value[file_name] += 2
            else:
                file_name_cheat_value[file_name] += 1

    if Sajjad_format_count > SAliB_format_count:
        return NORMAL_WIN_MESSAGE

    for file_name, count in file_name_cheat_value.items():
        if Sajjad_format_count + count > SAliB_format_count:
            return CHEAT_WIN_MESSAGE.format(file_name=file_name)

    return LOSE_MESSAGE
