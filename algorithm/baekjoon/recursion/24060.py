def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2       # q는 p, r의 중간 지점
        merge_sort(A, p, q)      # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)        # 병합

def merge(A, p, q, r):
    i = p
    j = q + 1
    t = 0
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        output_sequence.append(tmp[t])
        t += 1
            
    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp[t] = A[i]
        output_sequence.append(tmp[t])
        i += 1
        t += 1


    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp[t] = A[j]
        output_sequence.append(tmp[t])
        t+=1
        j+=1

    i = p
    t = 0
    while i <= r:  # 결과를 A[p..r]에 저장
        A[i] = tmp[t]
        i+=1
        t+=1

N, K = map(int, input().split())
A = list(map(int, input().split()))
tmp = [0 for _ in range(N)]
output_sequence = []
merge_sort(A, 0, len(A)-1)

if len(output_sequence) < K:
  print(-1)
else:
  print(output_sequence[K-1])