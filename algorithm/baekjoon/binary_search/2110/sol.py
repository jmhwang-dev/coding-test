# 2110
import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, C = map(int, input().split())
# print(N, C)

house_pos = []
for _ in range(N):
    house_pos.append(int(input()))

sorted_pos = sorted(house_pos)
# print(sorted_pos)

min_dist = 1
max_dist = sorted_pos[-1] - sorted_pos[0]

valid_max_dist = 1
curr_dist = 1

def check(sorted_pos, mid):
    cnt_c = 1
    curr_c_pos = 0
    for curr_index in range(1, N):

        adj_dist = sorted_pos[curr_index] - sorted_pos[curr_c_pos]
        if adj_dist >= mid:
            cnt_c += 1
            curr_c_pos = curr_index
        
    return cnt_c

while min_dist <= max_dist:
    mid = (max_dist - min_dist) // 2 + min_dist
    result = check(sorted_pos, mid)

    if result >= C:
        valid_max_dist = max(valid_max_dist, mid)
        min_dist = mid + 1
    else:
        max_dist = mid - 1
    
print(valid_max_dist)


## my sol
# import sys

# sys.stdin = open('input.txt', 'r')

# input = sys.stdin.readline

# N, C = map(int, input().split())
# # print(N, C)

# house_pos = []
# for _ in range(N):
#     house_pos.append(int(input()))

# sorted_pos = sorted(house_pos)
# # print(sorted_pos)

# min_dist = 1
# max_dist = sorted_pos[-1] - sorted_pos[0]

# valid_max_dist = 1
# curr_dist = 1

# def check(sorted_pos, mid):
#     cnt_c = 1
#     curr_c_pos = 0
#     for curr_index in range(1, N):

#         if cnt_c == C:
#             return cnt_c

#         adj_dist = sorted_pos[curr_index] - sorted_pos[curr_c_pos]
#         if adj_dist >= mid:
#             cnt_c += 1
#             curr_c_pos = curr_index
        
#     return cnt_c

# while min_dist <= max_dist:
#     mid = (max_dist - min_dist) // 2 + min_dist
#     result = check(sorted_pos, mid)

#     if result == C:
#         # if valid_max_dist > mid:
#         #     break

#         valid_max_dist = max(valid_max_dist, mid)
#         min_dist = mid + 1
#     else:
#         max_dist = mid - 1
    
# print(valid_max_dist)