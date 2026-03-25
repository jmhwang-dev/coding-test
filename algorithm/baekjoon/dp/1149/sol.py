import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
N = int(input())

RGB = [list(map(int, input().split())) for _ in range(N)]

dp = [RGB[0]]

for i in range(1, N):
    r,g,b = RGB[i]
    dp_r = r + min(dp[i-1][1], dp[i-1][2])
    dp_g = g + min(dp[i-1][0], dp[i-1][2])
    dp_b = b + min(dp[i-1][0], dp[i-1][1])
    
    dp_rgb = [dp_r, dp_g, dp_b]
    dp.append(dp_rgb)

print(min(dp[-1]))