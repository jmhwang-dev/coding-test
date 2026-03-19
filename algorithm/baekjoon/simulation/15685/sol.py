# 15685
import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
# print(N)

CURVES = [list(map(int, input().split())) for _ in range(N)]
# print(CURVES)

coords = set()

moves = [[1,0], [0,-1], [-1,0], [0,1]]

starts = []
curves = []

for row, col, d, g in CURVES:

    starts.append([row, col])
    curve = [d]
    for _ in range(g):
        new_curve = []
        for c in curve[::-1]:
            new_curve.append((c+1) % 4)
        curve += new_curve
    
    curves.append(curve)

for start, curve in zip(starts, curves):
    
    coords.add((start[0], start[1]))
    init_start = start

    for c in curve:
        new_coord = (init_start[0]+moves[c][0], init_start[1]+moves[c][1])
        coords.add(new_coord)
        init_start = new_coord

# print(coords)
count = 0
for x in range(100):
    for y in range(100):
        if (x,y) in coords and (x+1,y) in coords and (x,y+1) in coords and (x+1,y+1) in coords:
            count += 1

print(count)