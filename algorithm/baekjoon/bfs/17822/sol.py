import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, T = list(map(int, input().split()))

CIRCLES = [list(map(int, input().split())) for _ in range(N)]
ROTATE = [list(map(int, input().split())) for _ in range(T)]

# print(CIRCLES)
# print(ROTATE)

def rotate(rotate_info):
    global CIRCLES
    x, d, k = rotate_info

    for _ in range(k):
        for i in range(N):
            if (i+1) % x != 0:
                continue
            
            tmp_circle = [0] * M
            for j in range(M):

                if d == 0:
                    # ccw
                    new_index = (j + M-1) % M

                else:
                    # cw
                    new_index = (j + 1) % M
                    
                
                tmp_circle[j] = CIRCLES[i][new_index]
            
            CIRCLES[i] = tmp_circle
    return

def bfs():
    moves = [[-1,0], [1,0], [0,1], [0,-1]]
    is_exist = False
    for row in range(N):
        for col in range(M):
            if CIRCLES[row][col] == -1:
                continue

            curr_num = CIRCLES[row][col]
            queue = deque([[row, col]])
            while queue:
                curr_row, curr_col = queue.popleft()

                for dx, dy in moves:
                    new_row = curr_row + dx
                    new_col = curr_col + dy

                    if new_col < 0:
                        new_col = M-1
                    
                    elif new_col >= M:
                        new_col = 0


                    if not (0 <= new_row < N):
                        continue

                    if not (0 <= new_col < M):
                        continue

                    if CIRCLES[new_row][new_col] == curr_num:
                        is_exist = True
                        # print(curr_num, new_row, new_col)
                        CIRCLES[curr_row][curr_col] = -1
                        CIRCLES[new_row][new_col] = -1
                        queue.append([new_row, new_col])

    return is_exist


def update():
    total_sum = 0
    total_cnt = 0
    for row in range(N):
        for col in range(M):
            if CIRCLES[row][col] != -1:
                total_sum += CIRCLES[row][col]
                total_cnt += 1
    
    avg = total_sum / total_cnt if total_sum != 0 else 0

    for row in range(N):
        for col in range(M):
            if CIRCLES[row][col] == -1:
                continue

            if CIRCLES[row][col] > avg:
                CIRCLES[row][col] -= 1

            elif CIRCLES[row][col] < avg:
                CIRCLES[row][col] += 1

def get_sum():
    result = 0
    for row in range(N):
        for col in range(M):
            if CIRCLES[row][col] != -1:
                result += CIRCLES[row][col]
    return result

for roate_info in ROTATE:
    rotate(roate_info)
    is_exist = bfs()

    if not is_exist:
        update()

print(get_sum())