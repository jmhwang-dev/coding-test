import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = list(map(int, input().split()))
BOARD = [input().strip() for _ in range(N)]
# print(BOARD)

COIN_LOC = []
for row in range(N):
    for col in range(M):
        if BOARD[row][col] == 'o':
            COIN_LOC.append([row, col])

r1, c1 = COIN_LOC[0]
r2, c2 = COIN_LOC[1]

queue = deque([(r1, c1, r2, c2, 0)])
visited = set()
visited.add((r1, c1, r2, c2))
# print(coin_loc)

moves = [[-1,0],[0,-1],[1,0],[0,1]]

def move(r,c,dx,dy):
    new_r, new_c = r + dx, c + dy
    if not (0 <= new_r < N and 0 <= new_c < M):
        return new_r, new_c, 1
    
    if BOARD[new_r][new_c] == '#':
        return r, c, 0
    
    return new_r, new_c, 0

while queue:
    r1, c1, r2, c2, cnt = queue.popleft()

    if cnt >= 10:
        continue

    for dx, dy in moves:
        new_r1, new_c1, cnt1 = move(r1,c1,dx,dy)
        new_r2, new_c2, cnt2 = move(r2,c2,dx,dy)

        drop_cnt = cnt1 + cnt2

        if drop_cnt == 1:
            print(cnt + 1)
            exit()

        if drop_cnt == 2:
            continue
            
        new_coin_loc = (new_r1, new_c1, new_r2, new_c2)
        if new_coin_loc in visited:
            continue

        visited.add(new_coin_loc)
        queue.append((new_r1, new_c1, new_r2, new_c2, cnt+1))

print(-1)