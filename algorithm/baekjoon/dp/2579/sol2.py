import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
STEPS = [int(input()) for _ in range(N)]

if N == 1:
    print(STEPS[0])
    exit()

dp = [0] * (N+1)
dp[1] = STEPS[0]
dp[2] = dp[1] + STEPS[1]

for i in range(3, N+1):
    dp[i] = max(dp[i-2], dp[i-3] + STEPS[i-2]) + STEPS[i-1]
print(dp[N])