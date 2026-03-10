from pprint import pprint
import sys
from collections import deque

sys.stdin = open("input1.txt", "r")

input = sys.stdin.readline

N, M, CURR_FUEL = map(int, input().split())

BOARD = [list(map(int, input().split())) for _ in range(N)]

tx, ty = map(int, input().split())
TAXI_POS_DIST = [tx - 1, ty - 1, 0]
MOVES = [[-1, 0], [0,-1], [0,1], [1,0]]


def get_nearest_passenger(passengers):
    global CURR_FUEL, TAXI_POS_DIST
    visited = [[False] * N for _ in range(N)]
    visited[TAXI_POS_DIST[0]][TAXI_POS_DIST[1]] = True

    queue = deque([TAXI_POS_DIST])
    candidates = []

    while queue:
        if len(candidates) > 0:
            break
        len_queue = len(queue)
        for _ in range(len_queue):
            curr_tx, curr_ty, curr_dist = queue.popleft()

            if (curr_tx, curr_ty) in passengers:
                candidates.append((curr_tx, curr_ty, curr_dist))
                
            for dx, dy in MOVES:
                new_tx = curr_tx + dx
                new_ty = curr_ty + dy

                if not (0 <= new_tx < N) or not (0 <= new_ty < N):
                    continue

                if BOARD[new_tx][new_ty] != 0:
                    continue

                if visited[new_tx][new_ty]:
                    continue
                
                new_taxi_pos_dist = [new_tx, new_ty, curr_dist+1]
                queue.append(new_taxi_pos_dist)
                visited[new_tx][new_ty] = True
        
    if len(candidates) == 0:
        print(-1)
        exit()

    candidates.sort(key=lambda x: (x[0], x[1]))
    result = candidates[0]
    dist = result[-1]

    if dist > CURR_FUEL:
        print(-1)
        exit()

    CURR_FUEL -= dist
    return result[0:2]

def check_arrive(start, dst):
    global CURR_FUEL
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    start = list(start) + [0]

    queue = deque([start])

    while queue:
        len_queue = len(queue)
        for _ in range(len_queue):
            curr_tx, curr_ty, curr_dist = queue.popleft()

            if curr_dist > CURR_FUEL:
                print(-1)
                exit()

            if (curr_tx, curr_ty) == dst:
                return curr_dist
                
            for dx, dy in MOVES:
                new_tx = curr_tx + dx
                new_ty = curr_ty + dy

                if not (0 <= new_tx < N) or not (0 <= new_ty < N):
                    continue

                if BOARD[new_tx][new_ty] != 0:
                    continue

                if visited[new_tx][new_ty]:
                    continue
                
                new_taxi_pos_dist = [new_tx, new_ty, curr_dist+1]
                queue.append(new_taxi_pos_dist)
                visited[new_tx][new_ty] = True
    
    print(-1)
    exit()
    


if __name__=="__main__":
    passengers = {}
    for _ in range(M):
        sr, sc, er, ec = map(int, input().split())
        passengers[(sr - 1, sc - 1)] = (er - 1, ec - 1)

    while len(passengers) > 0:
        passenger_pos = get_nearest_passenger(passengers)
        dist = check_arrive(passenger_pos, passengers[passenger_pos])
        
        if dist > CURR_FUEL:
            print(-1)
            exit()
        
        CURR_FUEL -= dist
        CURR_FUEL += dist * 2

        TAXI_POS_DIST = list(passengers[passenger_pos]) + [0]
        del passengers[passenger_pos]

    print(CURR_FUEL)


# best
import sys
from collections import deque
input = sys.stdin.readline

N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
tx, ty = tx - 1, ty - 1

MOVES = [(-1,0),(0,-1),(0,1),(1,0)]

# BFS 하나로 통합 - 목적지가 여러 개면 가장 가까운 것 반환
def bfs(sx, sy, targets: set):
    visited = [[False]*N for _ in range(N)]
    visited[sx][sy] = True
    queue = deque([(sx, sy, 0)])

    while queue:
        x, y, d = queue.popleft()

        if (x, y) in targets:
            return (x, y, d)  # 첫 도달 = 최단거리 (레벨BFS 불필요)

        for dx, dy in MOVES:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, d+1))

    return None  # 도달 불가

# 단일 목적지도 set으로 감싸서 동일한 bfs 재사용
def bfs_single(sx, sy, tx, ty):
    return bfs(sx, sy, {(tx, ty)})


passengers = {}
for _ in range(M):
    sr, sc, er, ec = map(int, input().split())
    passengers[(sr-1, sc-1)] = (er-1, ec-1)

while passengers:
    # 가장 가까운 승객 탐색 (동거리면 행->열 오름차순)
    result = bfs(tx, ty, set(passengers.keys()))
    if result is None:
        print(-1); exit()

    px, py, dist_to_p = result

    # 거리가 같은 후보가 있을 수 있으므로 처리
    # (BFS는 최단거리 첫 도달이지만 동거리 후보 중 행/열 우선순위 필요)
    # → targets에 도달한 동일 dist 후보를 모두 수집 후 정렬
    visited = [[False]*N for _ in range(N)]
    visited[tx][ty] = True
    queue = deque([(tx, ty, 0)])
    candidates = []

    while queue:
        x, y, d = queue.popleft()
        if d > dist_to_p:
            break
        if (x, y) in passengers:
            candidates.append((x, y))
        for dx, dy in MOVES:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, d+1))

    candidates.sort()
    px, py = candidates[0]

    if dist_to_p > fuel:
        print(-1); exit()
    fuel -= dist_to_p

    # 승객 목적지까지 이동
    dst = passengers[(px, py)]
    result2 = bfs_single(px, py, dst[0], dst[1])
    if result2 is None or result2[2] > fuel:
        print(-1); exit()

    fuel -= result2[2]
    fuel += result2[2] * 2  # 연료 충전

    tx, ty = dst
    del passengers[(px, py)]

print(fuel)