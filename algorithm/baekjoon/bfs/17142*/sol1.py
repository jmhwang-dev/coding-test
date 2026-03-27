import sys
from itertools import combinations
from collections import deque

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = list(map(int, input().split()))

BOARD = [list(map(int, input().split())) for _ in range(N)]

def get_board_info():
    virus_pos = []
    empty_cnt = 0
    for row in range(N):
        for col in range(N):

            if BOARD[row][col] == 2:
                virus_pos.append([row, col])
            elif BOARD[row][col] == 0:
                empty_cnt += 1
    
    return virus_pos, empty_cnt

def init_time(pos):
    take_time_board = [[-1] * N for _ in range(N)]

    for row, col in pos:
        take_time_board[row][col] = 0

    return take_time_board

def get_infection_time(virus_pos, empty_cnt, m=M):
    moves = [[-1,0], [1,0], [0,1], [0,-1]]
    
    min_time = float('inf')
    for comb in combinations(virus_pos, m):
        queue = deque(list(comb))
        board = [BOARD[i][:] for i in range(N)]
        taken_time_board = init_time(comb)
        infected_cnt = 0
        taken_time = 0

        while queue:
            activation_cnt = len(queue)

            for _ in range(activation_cnt):
                curr_row, curr_col = queue.popleft()

                for dx, dy in moves:
                    new_row = curr_row + dx
                    new_col = curr_col + dy

                    if not (0 <= new_row < N) or not (0 <= new_col < N) or board[new_row][new_col] == 1:
                        continue

                    if taken_time_board[new_row][new_col] != -1:
                        continue

                    if board[new_row][new_col] == 0:
                        board[new_row][new_col] = 2
                        infected_cnt += 1

                    taken_time = taken_time_board[curr_row][curr_col] + 1
                    taken_time_board[new_row][new_col] = taken_time

                    if infected_cnt == empty_cnt:
                        min_time = min(min_time, taken_time)
                        break

                    queue.append([new_row, new_col])
        # for row in range(N):
        #     print(board[row])
        # print(taken_time)
        # print()

    return min_time if min_time != float('inf') else -1

virus_pos, emtpy_cnt = get_board_info()
if emtpy_cnt == 0:
    print(0)
    exit()

ans = get_infection_time(virus_pos, emtpy_cnt, M)
print(ans)