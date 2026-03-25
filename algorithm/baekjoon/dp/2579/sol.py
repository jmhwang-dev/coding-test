import sys

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
STEPS = [0] + [ int(input()) for _ in range(N)]
dp = [0] * (N + 1)

if N == 1:
    print(STEPS[1])
    exit()

if N == 2:
    print(STEPS[1]+STEPS[2])
    exit()

dp[1] = STEPS[1]
dp[2] = STEPS[1] + STEPS[2]
dp[3] = max(STEPS[1], STEPS[2]) + STEPS[3]

for i in range(4, N+1):
    dp[i] = max(dp[i-2], dp[i-3] + STEPS[i-1]) + STEPS[i]

print(dp[N])