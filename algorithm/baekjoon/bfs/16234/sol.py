import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, L, R = list(map(int, input().split()))

POPULATIONS = [list(map(int, input().split())) for _ in range(N)]
VISITED = [[False] * N for _ in range(N)]

def reset_visited():
    global VISITED
    for row in range(N):
        for col in range(N):
            VISITED[row][col] = False

def update_popluation():
    global POPULATIONS, VISITED
    adj_pos = [[0,1],[1,0], [-1,0], [0,-1]]
    updated = False
    for row in range(N):
        for col in range(N):

            if VISITED[row][col]:
                continue

            queue = deque([[row, col]])
            VISITED[row][col] = True

            cluster_sum = POPULATIONS[row][col]
            cluster_cnt = 1
            update_pos = [[row, col]]
            while queue:
                curr_row, curr_col = queue.popleft()

                for dx, dy in adj_pos:
                    new_row = curr_row + dx
                    new_col = curr_col + dy

                    if not (0<=new_row<N) or not (0<=new_col<N) or VISITED[new_row][new_col]:
                        continue

                    diff_poplulation = abs(POPULATIONS[curr_row][curr_col] - POPULATIONS[new_row][new_col])

                    if (L <= diff_poplulation <= R):
                        VISITED[new_row][new_col] = True
                        queue.append([new_row, new_col])
                        cluster_sum += POPULATIONS[new_row][new_col]
                        cluster_cnt += 1
                        update_pos.append([new_row, new_col])
            if len(update_pos) > 1:
                updated = True
            for ur, uc in update_pos:
                POPULATIONS[ur][uc] = cluster_sum // cluster_cnt
    if updated:
        return 1
    return 0

days = 0
while True:
    day = update_popluation()
    if day == 0:
        print(days)
        exit()
    else:
        days += day

    # print(days)
    # exit()
    reset_visited()

    # for i in range(N):
    #     print(POPULATIONS[i])
    
    # for i in range(N):
    #     print(VISITED[i])
    # exit()