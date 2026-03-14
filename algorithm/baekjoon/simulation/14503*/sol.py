import sys

# sys.stdin = open('input.txt') # 제출 시 주석 처리
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서 (0, 1, 2, 3)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0

while True:
    # 1. 현재 위치 청소
    if BOARD[r][c] == 0:
        BOARD[r][c] = 2 # 청소 완료 표시
        cnt += 1
    
    # 주변 4칸 확인
    found_uncleaned = False
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if BOARD[nr][nc] == 0:
                found_uncleaned = True
                break
    
    if not found_uncleaned:
        # 2. 청소되지 않은 빈칸이 없는 경우
        # 후진: 현재 방향(d)의 반대 방향
        back_r, back_c = r - dr[d], c - dc[d]
        
        # 후진 가능 여부 확인 (벽이 아니면 이동)
        if 0 <= back_r < N and 0 <= back_c < M and BOARD[back_r][back_c] != 1:
            r, c = back_r, back_c
        else:
            # 벽이라서 후진 못 하면 종료
            break
    else:
        # 3. 청소되지 않은 빈칸이 있는 경우
        # 반시계 90도 회전 (0->3, 3->2, 2->1, 1->0)
        d = (d + 3) % 4
        
        # 앞쪽 칸이 청소되지 않은 빈칸이면 전진
        front_r, front_c = r + dr[d], c + dc[d]
        if 0 <= front_r < N and 0 <= front_c < M and BOARD[front_r][front_c] == 0:
            r, c = front_r, front_c

print(cnt)