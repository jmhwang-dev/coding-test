import sys

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
MEETINGS = [list(map(int, input().split())) for _ in range(N)]

MEETINGS.sort(key=lambda x: (x[1], x[0]))

max_count = -float('inf')
last_end_time = 0
count = 0
for start, end in MEETINGS:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)