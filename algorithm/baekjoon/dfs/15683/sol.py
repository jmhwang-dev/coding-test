import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = list(map(int, input().split()))
BOARD = [list(map(int, input().split())) for _ in range(N)]
WATCH = [[0] * M for _ in range(N)]
# print(N, M, BOARD)
# exit()

base = [[-1,0], [0,1], [1,0], [0,-1]]

cam_dirs = [
    [],
    [[0], [1], [2], [3]],                   # 1
    [[0,2], [1,3]],                         # 2
    [[0,1], [0, 3], [1,2], [2,3]],          # 3
    [[0,1,2], [1,2,3], [0,1,3], [0,2,3]],   # 4
    [[0,1,2,3]]                             # 5
]

def find_cam():
    cam = []
    for row in range(N):
        for col in range(M):
            if (0 < BOARD[row][col] < 6):
                cam.append((BOARD[row][col], row, col))
    return cam

def init_watch():
    for row in range(N):
        for col in range(M):
            if BOARD[row][col] != 0:
                WATCH[row][col] = -1
    return

def watch(row, col, cam_dir, check):
    for d in cam_dir:
        dx, dy = base[d]
        curr_row = row + dx
        curr_col = col + dy

        while (0 <= curr_row < N and 0 <= curr_col < M and BOARD[curr_row][curr_col] != 6):
            WATCH[curr_row][curr_col] += check

            curr_row += dx
            curr_col += dy

def count_zero():
    return sum(row.count(0) for row in WATCH)

def debug():
    for row in range(N):
        print(WATCH[row])
    print()

def dfs(index):
    global min_zero
    if index == len(cams):
        min_zero = min(min_zero, count_zero())
        return
    
    cam_num, cam_row, cam_col = cams[index]

    for cam_dir in cam_dirs[cam_num]:
        watch(cam_row, cam_col, cam_dir, -1)
        dfs(index+1)
        watch(cam_row, cam_col, cam_dir, 1)

        
min_zero = float('inf')

init_watch()
cams = find_cam()
dfs(0)
print(min_zero)