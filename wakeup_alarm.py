# https://quera.org/problemset/190992?tab=description
# ---------------------------------------------------
curr = list(map(int, input().split(":")))
alarm = list(map(int, input().split(":")))

curr_sec = curr[0] * 3600 + curr[1] * 60 + curr[2]
alarm_sec = alarm[0] * 3600 + alarm[1] * 60 + alarm[2]

diff = (alarm_sec - curr_sec) % (24 * 3600)
if diff == 0:
    diff = 24 * 3600

print(f"{diff // 3600:02d}:{(diff % 3600)//60:02d}:{diff % 60:02d}")
