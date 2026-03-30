import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, K = list(map(int, input().split()))

COINS = [int(input()) for _ in range(N)]

start = 0
end = N-1
while start <= end:
    mid = (end + start) // 2

    if COINS[mid] > K:
        end = mid - 1
    else:
        start = mid + 1

cnt = 0
start = mid
total = K
while K != 0:
    cnt += K // COINS[start]
    K %= COINS[start]         # 나머지 한번에 계산
    start -= 1

print(cnt)