# https://quera.org/problemset/14580
# ----------------------------------

channels_count, current_channel_num, channel_change_count = map(
    int, input().strip().split()
)

channels: dict[int, str] = {}

for i in range(1, channels_count + 1):
    channel_name = input().strip()
    channels[i] = channel_name

final_channel_num = (current_channel_num + channel_change_count) % channels_count
final_channel_num = final_channel_num if final_channel_num != 0 else channels_count

print(channels.get(final_channel_num, "Channel Not Found"))
