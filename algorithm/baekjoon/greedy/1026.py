def get_minimum_s(A=[5, 15,100, 31, 39, 0, 0, 3, 26], B=[11, 12, 13, 2, 3, 4, 5, 9, 1]):
    sort_A = sorted(A)
    sort_B = sorted(B, reverse=True)
    total = 0
    for a, b in zip(sort_A, sort_B):
        total += a * b
    print(total)

N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

get_minimum_s(A, B)