import sys
import heapq

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, K = list(map(int, input().split()))

JEWELRY = [list(map(int, input().split())) for _ in range(N)]
BAGS = [int(input()) for _ in range(K)]

# print(N, K)
# print(JEWELRY)
# print(BAGS)
# exit()

sorted_bags = sorted(BAGS)
sorted_jewely = sorted(JEWELRY, key=lambda x: x[0])

pq = []
result = 0
start_index = 0
for bag_size in sorted_bags:
    while start_index < N:
        if sorted_jewely[start_index][0] > bag_size:
            break

        price = -sorted_jewely[start_index][1]
        heapq.heappush(pq, price)
        start_index += 1
    if len(pq) > 0:
        max_price = heapq.heappop(pq) * -1
        result += max_price
print(result)