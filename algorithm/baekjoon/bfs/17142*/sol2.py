import sys
from itertools import combinations
from collections import deque

sys.stdin = open('input.txt', 'r')

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

def init_dist(pos):
    dist = [[-1] * N for _ in range(N)]

    for row, col in pos:
        dist[row][col] = 0

    return dist

def get_infection_time(virus_pos, empty_cnt, m=M):
    moves = [[-1,0], [1,0], [0,1], [0,-1]]
    
    min_time = float('inf')
    for comb in combinations(virus_pos, m):
        queue = deque(comb)
        dist = init_dist(comb)
        infected_cnt = 0
        max_time = 0

        while queue:
    
            curr_row, curr_col = queue.popleft()

            if dist[curr_row][curr_col] >= min_time:
                break

            for dx, dy in moves:
                new_row = curr_row + dx
                new_col = curr_col + dy

                if not (0 <= new_row < N) or not (0 <= new_col < N) or dist[new_row][new_col] != -1:
                    continue

                if BOARD[new_row][new_col] == 1:
                    continue

                dist[new_row][new_col] = dist[curr_row][curr_col] + 1

                if BOARD[new_row][new_col] == 0:
                    infected_cnt += 1
                    max_time = dist[new_row][new_col]

                queue.append([new_row, new_col])

            if infected_cnt == empty_cnt:
                min_time = min(min_time, max_time)
                break

        # for row in range(N):
        #     print(dist[row])
        # print(max_time)
        # print()

    return min_time if min_time != float('inf') else -1

virus_pos, emtpy_cnt = get_board_info()
if emtpy_cnt == 0:
    print(0)
    exit()

ans = get_infection_time(virus_pos, emtpy_cnt, M)
print(ans)