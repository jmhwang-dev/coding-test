import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

dp = [[1,1] for _ in range(N)]

for i in range(1, N):
    print((dp[j][0] for j in range(i) if S[j] < S[i]))
    dp[i][0] = max((dp[j][0] for j in range(i) if S[j] < S[i]), default=0) + 1

for i in range(N-1, -1, -1):
    dp[i][1] = max((dp[j][1] for j in range(i+1, N) if S[j] < S[i]), default=0) + 1

max_cnt = 0
for value_cnt in dp:
    max_cnt = max(max_cnt, sum(value_cnt) - 1)
print(max_cnt)