import sys
from collections import deque
from itertools import combinations

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(N)]
MAX_COUNT = 0

def count_zero(board):
    cnt = 0
    for row in board:
        cnt += row.count(0)
        # for col in range(M):
        #     if board[row][col] == 0:
        #         count += 1
    return cnt

def bfs(board):
    moves = [[1,0], [0,1], [-1, 0], [0,-1]]

    virus_pos = []
    for row in range(N):
        for col in range(M):
            if board[row][col] != 2:
                continue
            virus_pos.append((row, col))

    queue = deque(virus_pos)

    while queue:
        row, col = queue.popleft()

        for dx, dy in moves:
            new_row = row + dx
            new_col = col + dy

            if not (0 <= new_row < N) or not (0 <= new_col < M) or board[new_row][new_col] != 0:
                continue

            board[new_row][new_col] = 2
            queue.append((new_row, new_col))
    return board

def get_zero_pos():
    zero_pos = []
    for row in range(N):
        for col in range(M):
            if BOARD[row][col] == 0:
                zero_pos.append((row, col))
    return zero_pos

def debug(board):
    for row in range(N):
        for col in range(M):
            print(board[row][col], end=' ')
        print()
    print()

zero_pos = get_zero_pos()

for pos in combinations(zero_pos, 3):
    board = [row[:] for row in BOARD]
    
    for wall_x, wall_y in pos:
        board[wall_x][wall_y] = 1
    infected_board = bfs(board)
    zero_count = count_zero(infected_board)
    MAX_COUNT = max(MAX_COUNT, zero_count)
    
print(MAX_COUNT)