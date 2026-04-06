import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = list(map(int, input().split()))

visited = [False] * (N+1)

def dfs():
    global result, N, M

    if len(result) == M:
        print(*result, sep=' ')
        return

    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        result.append(i)
        dfs()
        visited[i] = False
        result.pop()

result = []
dfs()