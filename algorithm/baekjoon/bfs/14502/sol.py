import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = list(map(int, input().split()))

BOARD = [list(map(int, input().split())) for _ in range(N)]

# print(BOARD)

# 0 은 빈 칸
# 1은 벽
# 2는 바이러스
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

zero_pos = []
for row in range(N):
    for col in range(M):
        if BOARD[row][col] == 0:
            zero_pos.append([row, col])

wall_pos = combinations(zero_pos, 3)

def set_wall(wpos):
    new_board = [BOARD[i][:] for i in range(N) ]
    for row, col in wpos:
        new_board[row][col] = 1
    return new_board

def count_zero(result_board):
    cnt = 0
    for row in range(N):
        for col in range(M):
            if result_board[row][col] == 0:
                cnt += 1
    return cnt

def bfs(new_board):
    moves = [[0,1], [1,0], [0,-1], [-1,0]]
    visited = [[False] * M for _ in range(N)]

    for row in range(N):
        for col in range(M):
            if new_board[row][col] != 2 or visited[row][col]:
                continue

            queue = deque([[row, col]])
            visited[row][col] = True

            while queue:
                curr_row, curr_col = queue.popleft()

                for dx, dy in moves:
                    adj_row = curr_row + dx
                    adj_col = curr_col + dy

                    if not (0<=adj_row<N) or not (0<=adj_col<M) or visited[adj_row][adj_col]:
                        continue

                    if new_board[adj_row][adj_col] != 0:
                        continue

                    new_board[adj_row][adj_col] = 2
                    visited[adj_row][adj_col] = True
                    queue.append([adj_row, adj_col])
    return new_board


max_cnt = 0
for wpos in wall_pos:
    new_board = set_wall(wpos)
    result_board = bfs(new_board)
    max_cnt = max(max_cnt, count_zero(result_board))

print(max_cnt)