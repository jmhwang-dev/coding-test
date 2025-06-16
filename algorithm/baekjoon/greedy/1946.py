import sys
# _grades = [[3, 2],[1, 4],[4, 1],[2, 3],[5, 5]]
_grades=[[3, 6],[7, 3],[4, 2],[1, 4],[5, 7],[2, 5],[6, 1]]
def get_max_N(grades=_grades):
    # if 
    sorted_grades = sorted(grades, key=lambda x: x[0])
    count = 1
    refer = sorted_grades[0][1]
    for grade in sorted_grades[1:]:
        if grade[1] < refer:
            count += 1
            refer = grade[1]

    print(count)

T = int(input())
dataset = []
for _ in range(T):
    data = []
    for _ in range(int(input())):
        data.append(list(map(int, sys.stdin.readline().split())))
    dataset.append(data)

for data in dataset:
    get_max_N(data)