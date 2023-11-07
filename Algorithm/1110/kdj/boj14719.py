# # 14:00 ~ 
# import sys
# read = sys.stdin.readline

# h, w = list(map(int, input().split()))
# block = list(map(int, input().split()))

# start_flag = False
# answer = 0
# wall = 0
# for i in block:
#   if start_flag == False and i > 0:
#     wall = i
#     start_flag = True
#     water = 0
#     continue
#   if start_flag == True:
#     if i<wall:
#       water += wall-i

#     else:
#       answer += water
#       print(water)
#       water = 0
#       wall = i

# print(answer)


import sys
read = sys.stdin.readline

h, w = list(map(int, input().split()))
blocks = list(map(int, input().split()))

# 양쪽에서 최대 높이를 계산합니다.
left_max = [0] * w
right_max = [0] * w

# 왼쪽에서 시작하는 최대 높이
max_height = 0
for i in range(w):
    if blocks[i] > max_height:
        max_height = blocks[i]
    left_max[i] = max_height

# 오른쪽에서 시작하는 최대 높이
max_height = 0
for i in range(w-1, -1, -1):
    if blocks[i] > max_height:
        max_height = blocks[i]
    right_max[i] = max_height

# 빗물의 양을 계산합니다.
water = 0
for i in range(w):
    water += min(left_max[i], right_max[i]) - blocks[i]

# print(left_max, right_max)
print(water)
