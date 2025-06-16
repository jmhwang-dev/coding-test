def A2B(A=100, B=40021):
   start = B
   count = 1
   while True:
    if start == A:
        return count
    elif start < A:
        return -1

    remainder = start % 10
    if remainder == 1:
        start = int(str(start)[:-1])
        count += 1
        continue

    remainder = start % 2
    if remainder != 0:
        return -1
    else:
        start = start // 2
        count += 1


A, B = map(int, input().split())
print(A2B(A, B))