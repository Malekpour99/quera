# Question link: https://quera.org/problemset/251440
# ------------------------------------------------------

# Solve 1 - brute force
# ------------------------------------------------------
# a, b, c = map(int, input().split("?"))

# if a == 1:
#     tmp = a + b
#     if c == 1:
#         print(tmp + c)
#     else: 
#         print(tmp * c)
# elif b == 1:
#     if a > c:
#         print(a * (b + c))
#     else:
#         print((a + b) * c)
# elif c == 1:
#     print(a * (b + c))
# else:
#     print(a * b * c)

# Solve 2
# ------------------------------------------------------
nums = list(map(int, input().split("?")))
result = 1
skip_next = False
skip_previous = False
for i in range(len(nums)):
    if skip_next:
        skip_next = False
        skip_previous = True
        continue
    
    if nums[i] == 1:
        try:
            next_num = nums[i+1]
            if i - 1 > -1:
                previous_num = nums[i-1]
            else:
                helper = nums[i] + nums[i+1]
                skip_next = True
                result *= helper
                continue
                
        except IndexError:
            if i == len(nums) - 1:
                if not skip_previous:
                    helper = nums[i] + nums[i-1]
                    result = result // nums[i-1] * helper
                else:
                    result += nums[i]
            continue
        
        if next_num < previous_num:
            helper = nums[i] + next_num
            skip_next = True
            result *= helper
        else:
            if not skip_previous:
                helper = nums[i] + previous_num
                result = result // nums[i-1] * helper
            else:
                helper = nums[i] + next_num
                skip_next = True
                result *= helper
    else:
        result *= nums[i]

print(result)
 