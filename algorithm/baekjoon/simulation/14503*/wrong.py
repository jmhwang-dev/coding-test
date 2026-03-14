import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

BOARD = [list(map(int, input().split())) for _ in range(N)]

directions = {
    0: (-1,0),
    1: (0,1),
    2: (1,0),
    3: (0,-1)} # 북동남서

ccw_directions = {
    directions[0]: 3,
    directions[1]: 0,
    directions[2]: 1,
    directions[3]: 2} # 서북동남

curr_r = r
curr_c = c
curr_d = d
cnt = 0

while BOARD[curr_r][curr_c] != 1:
    is_cleand_all = True

    print('before', curr_r, curr_c, curr_d)

    if BOARD[curr_r][curr_c] == 0:
        BOARD[curr_r][curr_c] = '#'
        cnt += 1

    tmp_dir = curr_d
    for _ in range(4):
        ccw_dir = ccw_directions[directions[tmp_dir]]
        ccw_x, ccw_y = directions[ccw_dir]
        tmp_dir = ccw_dir

        new_x = curr_r + ccw_x
        new_y = curr_c + ccw_y

        if not (0<=new_x<N) or not (0<=new_y<M):
            continue

        # 주변에 청소가 필요한 경우
        if BOARD[new_x][new_y] == 0:
            curr_d = tmp_dir
            curr_r = new_x
            curr_c = new_y
            is_cleand_all = False

            break
    
    if is_cleand_all:
        move_x, move_y = directions[curr_d]
        back_move_x = move_x * -1
        back_move_y = move_y * -1
        curr_r += back_move_x
        curr_c += back_move_y

    print('after', curr_r, curr_c, curr_d, is_cleand_all)

# print('---')
print(cnt)