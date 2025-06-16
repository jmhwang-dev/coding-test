# N = 8

# paper = [
#     [1, 1, 0, 0, 0, 0, 1, 1,],
#     [1, 1, 0, 0, 0, 0, 1, 1,],
#     [0, 0, 0, 0, 1, 1, 0, 0,],
#     [0, 0, 0, 0, 1, 1, 0, 0,],
#     [1, 0, 0, 0, 1, 1, 1, 1,],
#     [0, 1, 0, 0, 1, 1, 1, 1,],
#     [0, 0, 1, 1, 1, 1, 1, 1,],
#     [0, 0, 1, 1, 1, 1, 1, 1]
#     ]


TOTAL_BLUE = 0
TOTAL_WHITE = 0

def solution(N, paper):
    global TOTAL_BLUE
    global TOTAL_WHITE

    if N == 1:
        if paper[0][0] == 1:
            TOTAL_BLUE += 1
        else:
            TOTAL_WHITE += 1
        return

    local_count = N**2
    local_blue_count = 0

    blue = 1
    for row in paper:
        local_blue_count += row.count(blue)

    if local_blue_count == local_count:
        TOTAL_BLUE += 1
    elif local_blue_count == 0:
        TOTAL_WHITE += 1
    else:
        half = N // 2
        left_top_paper = list(map(lambda x: x[:half], paper[:half]))
        right_top_paper = list(map(lambda x: x[half:], paper[:half]))
        left_bottom_paper = list(map(lambda x: x[:half], paper[half:]))
        right_bottom_paper = list(map(lambda x: x[half:], paper[half:]))

        solution(half, left_top_paper)
        solution(half, right_top_paper)
        solution(half, left_bottom_paper)
        solution(half, right_bottom_paper)

N = int(input())
paper = []
for _ in range(N):
    colors = list(map(int, input().split()))
    paper.append(colors)

solution(N, paper)
print(TOTAL_WHITE, TOTAL_BLUE, end='\n')