from pprint import pprint
import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())

BOARD = [list(map(int, input().split())) for _ in range(N)]
VISITED = [[False] * M for _ in range(N)]
MAX_VALUE = 0
moves = [[0,1], [1,0], [-1,0], [0,-1]]

def dfs(row, col, depth, curr_sum):
    global MAX_VALUE, VISITED
    
    if depth == 4:
        MAX_VALUE = max(MAX_VALUE, curr_sum)
        return
    
    VISITED[row][col] = True

    for dx, dy in moves:
        new_row = row + dx
        new_col = col + dy
        if not (0<=new_row<N) or not (0<=new_col<M) or VISITED[new_row][new_col]:
            continue
        dfs(new_row, new_col, depth+1, curr_sum + BOARD[new_row][new_col])

    VISITED[row][col] = False

from itertools import combinations

def extra_shape(row, col, curr_sum):
    global MAX_VALUE
    for combo in combinations(moves, 3):  # 4방향 중 3개 조합, 딱 4가지
        total = curr_sum
        valid = True
        for dx, dy in combo:
            nr, nc = row+dx, col+dy
            if not (0<=nr<N and 0<=nc<M):
                valid = False
                break
            total += BOARD[nr][nc]
        if valid:
            MAX_VALUE = max(MAX_VALUE, total)

for row in range(N):
    for col in range(M):
        dfs(row, col, 1, BOARD[row][col])
        extra_shape(row, col, BOARD[row][col])   # ㅗ ㅜ ㅏ ㅓ

print(MAX_VALUE)