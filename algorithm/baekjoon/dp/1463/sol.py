# 1463
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N = int(input())

memo = [0] * (N + 1)
memo[0] = -1 # not used
memo[1] = 0

for num in range(2, N+1):
    divide_3 = float('inf')
    divide_2 = float('inf')

    if num % 3 == 0:
        divide_3 = memo[num//3]
    
    if num % 2 == 0:
        divide_2 = memo[num//2]
    
    memo[num] = min(divide_3, divide_2, memo[num-1]) + 1

print(memo[N])