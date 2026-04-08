import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = list(map(int, input().split()))

result = []

def dfs():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N+1):
        result.append(i)
        dfs()
        result.pop()
    return

dfs()