# 최악 시간복잡도	O(n log n)
# 공간복잡도	О(n)

def merge_sort(A):
  if len(A) <= 1:
     return A
  
  mid = len(A) // 2
  
  left_half = merge_sort(A[:mid])
  right_half = merge_sort(A[mid:])
  return merge(left_half, right_half)

def merge(left, right):
  global OUTPUT
  merged = []

  left_index, right_index = 0, 0
  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      value = left[left_index]
      left_index += 1
    else:
      value = right[right_index]
      right_index += 1

    merged.append(value)
    OUTPUT.append(value)

  if left_index < len(left):
    OUTPUT += left[left_index:]
    merged += left[left_index:]
  if right_index < len(right):
    OUTPUT += right[right_index:]
    merged += right[right_index:]

  return merged

OUTPUT = []
N, K = map(int, input().split())
import sys
A = list(map(int, sys.stdin.readline().split()))

merge_sort(A)
print(OUTPUT)
# if len(OUTPUT) < K:
#   print(-1)
# else:
#   print(OUTPUT[K-1])