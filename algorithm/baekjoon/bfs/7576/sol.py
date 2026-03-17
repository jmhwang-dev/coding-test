# 7576
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

M, N = map(int, input().split())
# print(N, M)
BOARD = [list(map(int, input().split())) for _ in range(N)]
# print(BOARD)


good_tomato = []
for row in range(N):
    for col in range(M):
        if BOARD[row][col] == 1:
            good_tomato.append([row, col])

queue = deque(good_tomato)
days = -1

adj_pos = [[0,1], [1,0], [-1,0], [0,-1]]

while queue:
    curr_toamto_count = len(queue)

    for _ in range(curr_toamto_count):
        curr_row, curr_col = queue.popleft()

        for dx, dy in adj_pos:
            new_row = curr_row + dx
            new_col = curr_col + dy

            if not (0<=new_row<N) or not (0<=new_col<M):
                continue

            if BOARD[new_row][new_col] == 0:
                BOARD[new_row][new_col] = 1
                queue.append([new_row, new_col])
    # print(days)
    days += 1

for row in range(N):
    for col in range(M):
        if BOARD[row][col] == 0:
            print(-1)
            exit()

print(days)