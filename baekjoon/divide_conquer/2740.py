A = [
    [1, 2],
    [3, 4],
    [5, 6]
]

B = [
    [-1, -2, 0],
    [0, 0, 3]
]

def product(row, col, ans):
    pass

def solution(A, B):
    ans = []
    col = [0 for _ in range(len(B[0]))]

    for _ in range(len(A)):
        ans.append(col)

    for i, row in enumerate(A):
        cols = list(map(lambda x: x[0], B))

print(solution(A, B))