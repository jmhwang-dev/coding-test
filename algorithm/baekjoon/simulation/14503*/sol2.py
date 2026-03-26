import sys
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = list(map(int, input().split()))
r, c ,d = list(map(int, input().split()))
BOARD = [list(map(int, input().split())) for _ in range(N)]
# VISITED = [[False] * M for _ in range(N)]
# print(VISITED)
# print(BOARD)

moves = [[-1,0], [0,1], [1,0], [0,-1]] # 북동남서
# 0 -> 2
# 1 -> 3
# 2 -> 1
# 3 -> 0
move_back = [[1,0], [0, -1], [-1,0], [0, 1]]

# # ccw
# 0 -> d+3 % 4 -> 3
# 1 -> 4 -> 0
# 2 -> 1
# 3 -> 2

queue = deque([[r,c]])
cnt = 0
while queue:
    curr_row, curr_col = queue.popleft()

    if BOARD[curr_row][curr_col] == 0:
        cnt += 1
        BOARD[curr_row][curr_col] = 2 # 청소는 2, 벽 1, 청소안됨 0

    curr_direction = d
    to_clean_move = None

    rotate_cnt = 0
    while rotate_cnt < 4:
        curr_direction = (curr_direction + 3) % 4
        dx, dy = moves[curr_direction]
        new_row = curr_row + dx
        new_col = curr_col + dy

        if not (0<=new_row<N) or not (0<=new_col<M) or BOARD[new_row][new_col] != 0:
            # 반시계 방향으로 90 회전한다.
            rotate_cnt += 1
            continue

        else:
            to_clean_move = [new_row, new_col]
            break
    
    if to_clean_move is None: # 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        dx, dy = move_back[d]
        new_row = curr_row + dx
        new_col = curr_col + dy

        if not (0<=new_row<N) or not (0<=new_col<M) or BOARD[new_row][new_col] == 1:
            print(cnt)
            exit()

        queue.append([new_row, new_col])

    else: #현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
        d = curr_direction
        new_row, new_col = to_clean_move
        queue.append(to_clean_move)
    
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        # 1번으로 돌아간다.

print(cnt)