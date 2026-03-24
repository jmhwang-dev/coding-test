# 21609

import sys
from collections import deque
from pprint import pprint

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
N, M = list(map(int,input().split()))

BOARD = [list(map(int, input().split())) for _ in range(N)]
VISITED = [[False] * N for _ in range(N)]

def debug():
    for i in range(N):
        print(BOARD[i])
    print()

def roatate_ccw():
    ccw = [list(i) for i in zip(*BOARD)][::-1]
    # cw = [i for i in zip(*BOARD[::-1])]
    return ccw

def reset_rainbow():
    global VISITED
    for i in range(N):
        for j in range(N):
            if BOARD[i][j] == 0:
                VISITED[i][j] = False

def find_group(row, col, curr_color):
    global VISITED
    queue = deque([[row,col]])
    block_pos = [[row,col]]
    VISITED[row][col] = True
    moves = [[-1,0], [0,1], [1,0], [0,-1]]
    curr_block_size = 1
    curr_rainbow_size = 0

    while queue:
        curr_row, curr_col = queue.popleft()

        for dx, dy in moves:
            adj_row = curr_row + dx
            adj_col = curr_col + dy
            new_pos = [adj_row, adj_col]

            if not (0 <= adj_row < N) or not (0 <= adj_col < N) or VISITED[adj_row][adj_col]:
                continue

            if BOARD[adj_row][adj_col] == -1:
                continue

            # 색상이 같거나 무지개 블록일 때만 방문 처리 및 큐에 삽입
            if BOARD[adj_row][adj_col] == curr_color or BOARD[adj_row][adj_col] == 0:
                VISITED[adj_row][adj_col] = True
                curr_block_size += 1
                block_pos.append(new_pos)
                queue.append(new_pos)
                
                if BOARD[adj_row][adj_col] == 0:
                    curr_rainbow_size += 1

    return curr_block_size, curr_rainbow_size, block_pos

def find_max_group():
    global result, VISITED
    # 1. 매 턴 시작 시 방문 배열 완전히 초기화
    VISITED = [[False] * N for _ in range(N)]
    dict_group = {}
    for row  in range(N):
        for col in range(N):
            if not (1 <= BOARD[row][col] <= M):
                continue
            curr_block_size, curr_rainbow_size, block_pos = find_group(row, col, BOARD[row][col])
            reset_rainbow()

            if curr_block_size < 2:
                continue
            dict_group[(curr_block_size, curr_rainbow_size, row, col)] = block_pos
    
    if len(dict_group) == 0:
        print(result)
        exit()

    max_group = sorted(list(dict_group.keys()))[-1]
    return dict_group[max_group]

def get_score(max_group):
    score = len(max_group) * len(max_group)
    return score

def delete_block(max_group):
    global BOARD
    for x, y in max_group:
        BOARD[x][y] = -2

def apply_gravity():
    global BOARD
    for col in range(N):
        bottom = N - 1
        for row in range(N-1, -1, -1):

            if BOARD[row][col] == -1:
                bottom = row - 1
            elif BOARD[row][col] >= 0:
                
                if row != bottom:
                    BOARD[bottom][col], BOARD[row][col] = BOARD[row][col], -2

                bottom -= 1

result = 0
while True:
    max_group = find_max_group()
    result += get_score(max_group)
    delete_block(max_group)
    # debug()
    apply_gravity()
    BOARD = roatate_ccw()
    apply_gravity()

# debug()
# debug()