# 16236

import sys
from collections import deque
import heapq

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]

curr_eat = 0
result = 0
col_len = len(BOARD[0])
moves = [[0,1], [1,0], [-1,0], [0,-1]]

def find_init_shark_location():
    for row in range(N):
        for col in range(col_len):
            if BOARD[row][col] == 9:
                BOARD[row][col] = 0
                return [row, col]

def find_smaller_fish_location(curr_size):
    smaller_fish_pos = []
    for row in range(N):
        for col in range(col_len):
            if (0 < BOARD[row][col] < curr_size):
                smaller_fish_pos.append([row, col])
    return smaller_fish_pos

def find_nearest_fish(shark_pos, smaller_fish_pos):
    curr_row, curr_col = shark_pos
    
    visited = [ [False] * col_len for _ in range(N) ]
    visited[curr_row][curr_col] = True
    init_info = [0, curr_row, curr_col]
    queue = deque([init_info])
    pr = []

    while queue:
        curr_dist, curr_row, curr_col = queue.popleft()

        for dx, dy in moves:
            new_row = curr_row + dx
            new_col = curr_col + dy
            new_dist = curr_dist + 1

            if not (0<=new_row<N) or not (0<=new_col<col_len) or BOARD[new_row][new_col] > curr_size:
                continue

            if visited[new_row][new_col]:
                continue

            if [new_row, new_col] in smaller_fish_pos:
                heapq.heappush(pr, [new_dist, new_row, new_col])

            queue.append([new_dist, new_row, new_col])
            visited[new_row][new_col] = True
    
    if len(pr) == 0:
        print(result)
        exit()

    nearest_fish_info = heapq.heappop(pr)
    
    return nearest_fish_info

if __name__=="__main__":
    curr_size = 2
    smaller_fish_pos = find_smaller_fish_location(curr_size)

    if len(smaller_fish_pos) == 0:
        print(result)
        exit()

    shark_pos = find_init_shark_location()
    # print('curr_size:', curr_size, 'curr_eat:', curr_eat, 'result:', result, 'shark_pos:', shark_pos)
    while smaller_fish_pos:
        taken_time, fish_row, fish_col = find_nearest_fish(shark_pos, smaller_fish_pos)
        shark_pos = [fish_row, fish_col]
        BOARD[fish_row][fish_col] = 0
        result += taken_time
        curr_eat += 1

        if curr_eat == curr_size:
            curr_size += 1
            curr_eat = 0

        smaller_fish_pos = find_smaller_fish_location(curr_size)
        # print('curr_size:', curr_size, 'curr_eat:', curr_eat, 'result:', result, 'shark_pos:', shark_pos)
    
    print(result)   # 60