import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

# BOARD = [list(input().strip()) for _ in  range(N)]
BOARD = [list(input()) for _ in  range(N)]

# print(BOARD)

row = 0
col = 0

queue = deque([[row, col, 1]])
moves = [[0,1], [1,0], [-1, 0], [0, -1]]
BOARD[row][col] = '#'

while queue:
    curr_row, curr_col, curr_dist = queue.popleft()

    if curr_row == N-1 and curr_col == M-1:
        print(curr_dist)
        exit()

    for dx, dy in moves:
        new_row = curr_row + dx
        new_col = curr_col + dy

        if not (0<=new_row<N) or not (0<=new_col<M) or BOARD[new_row][new_col] != '1':
            continue
        
        queue.append([new_row, new_col, curr_dist + 1])
        BOARD[new_row][new_col] = '#'
    