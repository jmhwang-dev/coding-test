import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = list(map(int, input().split()))

def dfs(num):
    if len(result) == M:
        print(*result)
        return

    for i in range(num, N+1):
        result.append(i)
        dfs(i+1)
        result.pop()

result = []
dfs(1)