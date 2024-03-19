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
  merged = []

  left_index, right_index = 0, 0
  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      merged.append(left[left_index])
      left_index += 1
    else:
      merged.append(right[right_index])
      right_index += 1
    
  merged += left[left_index:]
  merged += right[right_index:]

  return merged

A = [4,5,1,3,2]
print(merge_sort(A))