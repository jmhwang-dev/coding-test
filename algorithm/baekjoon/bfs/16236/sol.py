# 16236

import sys
from collections import deque
import heapq

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]

curr_eat = 0
result = 0
col_len = len(BOARD[0])
moves = [[0,1], [1,0], [-1,0], [0,-1]]

def find_init_shark_location():
    for row in range(N):
        for col in range(col_len):
            if BOARD[row][col] == 9:
                BOARD[row][col] = 0
                return [row, col]

def find_smaller_fish_location(curr_size):
    smaller_fish_pos = []
    for row in range(N):
        for col in range(col_len):
            if (0 < BOARD[row][col] < curr_size):
                smaller_fish_pos.append([row, col])
    return smaller_fish_pos

def find_nearest_fish(shark_pos, smaller_fish_pos):
    curr_row, curr_col = shark_pos
    
    visited = [ [False] * col_len for _ in range(N) ]
    visited[curr_row][curr_col] = True
    init_info = [0, curr_row, curr_col]
    queue = deque([init_info])
    pr = []

    while queue:
        curr_dist, curr_row, curr_col = queue.popleft()

        for dx, dy in moves:
            new_row = curr_row + dx
            new_col = curr_col + dy
            new_dist = curr_dist + 1

            if not (0<=new_row<N) or not (0<=new_col<col_len) or BOARD[new_row][new_col] > curr_size:
                continue

            if visited[new_row][new_col]:
                continue

            if [new_row, new_col] in smaller_fish_pos:
                heapq.heappush(pr, [new_dist, new_row, new_col])

            queue.append([new_dist, new_row, new_col])
            visited[new_row][new_col] = True
    
    if len(pr) == 0:
        print(result)
        exit()

    nearest_fish_info = heapq.heappop(pr)
    
    return nearest_fish_info

if __name__=="__main__":
    curr_size = 2
    smaller_fish_pos = find_smaller_fish_location(curr_size)

    if len(smaller_fish_pos) == 0:
        print(result)
        exit()

    shark_pos = find_init_shark_location()
    # print('curr_size:', curr_size, 'curr_eat:', curr_eat, 'result:', result, 'shark_pos:', shark_pos)
    while smaller_fish_pos:
        taken_time, fish_row, fish_col = find_nearest_fish(shark_pos, smaller_fish_pos)
        shark_pos = [fish_row, fish_col]
        BOARD[fish_row][fish_col] = 0
        result += taken_time
        curr_eat += 1

        if curr_eat == curr_size:
            curr_size += 1
            curr_eat = 0

        smaller_fish_pos = find_smaller_fish_location(curr_size)
        # print('curr_size:', curr_size, 'curr_eat:', curr_eat, 'result:', result, 'shark_pos:', shark_pos)
    
    print(result)   # 60


### best


import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)] # 상, 좌, 하, 우

# 1. 상어 초기 위치 찾기 및 보드 초기화
shark_r, shark_c = 0, 0
for i in range(N):
    for j in range(N):
        if BOARD[i][j] == 9:
            shark_r, shark_c = i, j
            BOARD[i][j] = 0

curr_size = 2
curr_eat = 0
total_time = 0

def find_best_fish(start_r, start_c, size):
    visited = [[False] * N for _ in range(N)]
    queue = deque([(0, start_r, start_c)])
    visited[start_r][start_c] = True
    
    candidates = []
    min_dist = float('inf')
    
    while queue:
        dist, r, c = queue.popleft()
        
        # [핵심 최적화 1] 이미 찾은 물고기보다 거리가 멀어지면 탐색 즉시 중단
        if dist > min_dist:
            break
            
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 지나갈 수 있는 조건: 물고기가 상어 크기 이하이거나 빈 칸
                if BOARD[nr][nc] <= size:
                    visited[nr][nc] = True
                    
                    # [핵심 최적화 2] in 연산자 없이 보드 값만으로 1번의 연산에 확인
                    if 0 < BOARD[nr][nc] < size:
                        min_dist = dist # 첫 물고기를 찾은 시점의 거리를 최단 거리로 고정
                        candidates.append((nr, nc))
                    else:
                        # 먹을 수는 없지만 지나갈 수 있다면 큐에 추가 (최단 거리가 갱신되지 않았을 때만)
                        queue.append((dist + 1, nr, nc))
                        
    if not candidates:
        return None
        
    # 같은 최단 거리 내에서 가장 위, 가장 왼쪽 기준 정렬 (행 오름차순, 열 오름차순)
    candidates.sort()
    best_r, best_c = candidates[0]
    return (min_dist + 1, best_r, best_c)

# 메인 시뮬레이션 루프
while True:
    result = find_best_fish(shark_r, shark_c, curr_size)
    
    if result is None: # 더 이상 먹을 수 있는 물고기가 없음 (고립 상태 포함)
        break
        
    time_taken, fish_r, fish_c = result
    
    # 상어 상태 업데이트
    total_time += time_taken
    curr_eat += 1
    if curr_eat == curr_size:
        curr_size += 1
        curr_eat = 0
        
    BOARD[fish_r][fish_c] = 0 # 물고기 먹음
    shark_r, shark_c = fish_r, fish_c # 상어 이동

print(total_time)