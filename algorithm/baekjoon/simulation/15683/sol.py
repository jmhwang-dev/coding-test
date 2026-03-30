import sys
from itertools import product


sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = list(map(int, input().split()))
BOARD = [list(map(int, input().split())) for _ in range(N)]
# print(N, M, BOARD)
# exit()

# 각 CCTV 타입별로 가능한 방향 조합 (0:우, 1:하, 2:좌, 3:상 기준 예시)
directions = [[0,1], [-1,0], [0,-1], [1,0]]

modes = [
    [], # 0번 인덱스 버림
    [[0], [1], [2], [3]],            # 1번 CCTV
    [[0, 2], [1, 3]],                # 2번 CCTV
    [[0, 3], [0, 1], [1, 2], [2, 3]], # 3번 CCTV
    [[0, 2, 3], [0, 1, 3], [0, 1, 2], [1, 2, 3]], # 4번 CCTV
    [[0, 1, 2, 3]]                   # 5번 CCTV
]

cctv_list = []
for row in range(N):
    for col in range(M):
        if (1 <= BOARD[row][col] < 6):
            cctv_list.append((BOARD[row][col], row, col))

possible_directions = []
for cctv_type, r, c in cctv_list:
    possible_directions.append(modes[cctv_type])

def simulate(combo):
    global min_zero
    new_board = [BOARD[i][:] for i in range(N)]

    for i in range(len(combo)):
        for d in combo[i]:
            new_board = watch(cctv_list[i], directions[d], new_board)
    
    min_zero = min(min_zero, count_zero(new_board))

def count_zero(board):

    cnt = 0
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                cnt += 1
    return cnt

def watch(cctv_info, direction, board):
    cctv_type, r, c = cctv_info
    dx, dy = direction

    curr_row = r
    curr_col = c

    while (0 <= curr_row < N and 0 <= curr_col < M) and board[curr_row][curr_col] != 6:
        board[curr_row][curr_col] = '#'
        curr_row += dx
        curr_col += dy    
    
    return board
    
min_zero = float('inf')

for combo in product(*possible_directions):
    simulate(combo)

print(min_zero)