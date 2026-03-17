import sys

sys.stdin = open('./input.txt', 'r')

input = sys.stdin.readline

N, M  = map(int, input().split())
# print(N, M)

tree_heights = list(map(int, input().split()))
# print(tree_heights)

low = 0
high = max(tree_heights)

cutter_height = 0
while low <= high:

    mid = (high - low) // 2 + low

    total_count = 0

    total_count = sum(height - mid for height in tree_heights if height - mid > 0)

    if total_count >= M:
        low = mid + 1
        cutter_height = max(cutter_height, mid)

    else:
        high = mid - 1

print(cutter_height)