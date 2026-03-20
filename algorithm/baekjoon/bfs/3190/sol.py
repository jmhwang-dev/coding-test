import sys
from collections import deque

sys.stdin = open('input.txt','r')
input = sys.stdin.readline
N = int(input())

K = int(input())
BOARD = [[0] * N for _ in range(N)]
BOARD[0][0] = 2
for _ in range(K):
    apple_x, apple_y = list(map(int, input().split()))
    BOARD[apple_x-1][apple_y-1] = 1

L = int(input())
dir_info = {}
for _ in range(L):
    time, direction = input().split()
    dir_info[int(time)] = direction

moves = [[0,1], [1,0], [0, -1], [-1,0]] # 우하좌상
curr_time = 0
curr_dir = 0

queue = deque([[0,0]])

while True:
    curr_row, curr_col = queue[-1]

    if curr_time in dir_info:
        if dir_info[curr_time] == 'D':
            curr_dir = (curr_dir+1) % 4
        if dir_info[curr_time] == 'L':
            curr_dir = (curr_dir-1) % 4

    dx, dy = moves[curr_dir]
    new_row = curr_row + dx
    new_col = curr_col + dy
    new_pos = [new_row, new_col]

    if not (0<= new_row < N) or not (0<= new_col < N) or BOARD[new_row][new_col] == 2:
        curr_time += 1
        break
    
    if BOARD[new_row][new_col] != 1:
        tail_row, tail_col = queue.popleft()
        BOARD[tail_row][tail_col] = 0
    
    queue.append(new_pos)
    BOARD[new_row][new_col] = 2

    # print(new_pos, len(queue))
    curr_time += 1

print(curr_time)