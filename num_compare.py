# https://quera.org/problemset/3406
# ---------------------------------

first_num_str = input().strip()
first_num_value = int(first_num_str[::-1])

second_num_str = input().strip()
second_num_value = int(second_num_str[::-1])

if second_num_value < first_num_value:
    print(f"{second_num_str} < {first_num_str}")
elif first_num_value < second_num_value:
    print(f"{first_num_str} < {second_num_str}")
else:
    print(f"{first_num_str} = {second_num_str}")
