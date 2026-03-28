import sys
from collections import defaultdict, deque
from itertools import combinations

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
POPULATIONS = list(map(int, input().split()))
LOCATIONS = [list(map(int, input().split())) for _ in range(N)]

# print(N, POPULATIONS, LOCATIONS)
graph = defaultdict(list)

for i, loc in enumerate(LOCATIONS, 1):
    graph[i] = loc[1:]

min_population = float('inf')
nodes = [i for i in range(1, N+1)]

def dfs(node, group, visited):
    visited.add(node)
    for adj in graph[node]:
        if adj in group and adj not in visited:
            dfs(adj, group, visited)

def is_connected(group):
    visited = set()
    dfs(group[0], group, visited)
    return len(group) == len(visited)

min_sum = float('inf')
for i in range(1, N):
    for group1 in combinations(nodes, i):
        group2 = list(set(nodes) - set(group1))
        if is_connected(group1) and is_connected(group2):
            group1_sum = sum(POPULATIONS[i-1] for i in group1)
            group2_sum = sum(POPULATIONS[i-1] for i in group2)
            min_sum = min(min_sum, abs(group1_sum - group2_sum))
            
print(-1 if min_sum == float('inf') else min_sum)
