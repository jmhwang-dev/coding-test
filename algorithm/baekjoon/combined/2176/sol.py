import sys
import collections
from collections import deque
import heapq
from pprint import pprint

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

S, T = 1, 2
N, M = map(int, input().split())

EDGES = [list(map(int, input().split())) for _ in range(M)]
VISITED = [False] * N

def get_graph():
    global EDGES
    graph = collections.defaultdict(list)
    for start, end, dist in EDGES:
        graph[start].append([end, dist])
        graph[end].append([start, dist])

    return graph

def get_shortest_dist(graph):
    global S, T, N
    dist = [float('inf')] * N

    pq = [[0, T]]
    dist[T-1] = 0

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if dist[curr_node-1] < curr_dist:
            continue

        for adj_node, adj_dist in graph[curr_node]:
            index = adj_node - 1
            new_dist = curr_dist + adj_dist

            if dist[index] < new_dist:
                continue

            dist[index] = new_dist
            heapq.heappush(pq, [new_dist, adj_node])

    return dist

memo = [-1] * N
def dfs(dist, curr_node):
    global T

    if curr_node == T:
        return 1
    
    if memo[curr_node-1] != -1:
        return memo[curr_node-1]
    
    path_count = 0
    for adj_node, _ in graph[curr_node]:
        if dist[curr_node-1] > dist[adj_node-1]:
            path_count += dfs(dist, adj_node)

    memo[curr_node-1] = path_count
    return path_count

graph = get_graph()
dist = get_shortest_dist(graph)
print(dfs(dist, S))