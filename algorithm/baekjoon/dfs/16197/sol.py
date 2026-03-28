import sys

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
# print(coin_loc)

moves = [[-1,0],[0,-1],[1,0],[0,1]]
min_cnt = float('inf')

def move(coin_loc, cnt):
    global min_cnt
    if cnt > 10 or cnt >= min_cnt:
        return
    
    drop_cnt = 0
    for curr_row, curr_col in coin_loc:
        if not (0 <= curr_row < N) or not (0 <= curr_col < M):
            drop_cnt += 1
    
    if drop_cnt == 1:
        min_cnt = min(min_cnt, cnt)
        return
    
    elif drop_cnt == 2:
        return
    
    for dx, dy in moves:
        new_coin_loc = []
        for curr_row, curr_col in coin_loc:
            new_row = curr_row + dx
            new_col = curr_col + dy
            
            if (0 <= new_row < N) and (0 <= new_col < M):
                if BOARD[new_row][new_col] == '#':
                    new_row = curr_row
                    new_col = curr_col
            
            new_coin_loc.append([new_row, new_col])
        move(new_coin_loc, cnt+1)
    return

move(COIN_LOC, 0)
print(-1) if min_cnt == float('inf') else print(min_cnt)