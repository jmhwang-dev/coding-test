import sys
import heapq
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
LECTURES = [list(map(int, input().split())) for _ in range(N)]

LECTURES.sort(key=lambda x: (x[0], x[1]))
# print(LECTURES)

pq = []
heapq.heappush(pq, LECTURES[0][1])
for start, end in LECTURES[1:]:

    if pq[0] <= start:
        heapq.heappop(pq)
    heapq.heappush(pq, end)
print(len(pq))
