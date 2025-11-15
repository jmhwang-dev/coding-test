class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        n_start = 0
        m_start = 0
        m_end = m
        while True:
            if n_start == n:
                return
            
            if m_start == m_end:
                nums1[m_start:] = nums2[n_start:]
                return

            if nums1[m_start] > nums2[n_start]:
                nums1[m_start+1:m_end+1] = nums1[m_start:m_end]
                nums1[m_start] = nums2[n_start]
                n_start += 1
                m_end += 1
            
            m_start += 1


# ans2
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            nums1[:] = nums2[:]
            return
        if n == 0:
            return

        while True:
            print("nums1: ", nums1, "   nums2:", nums2, "   m:", m, "   n:", n)

            if m == 0:
                nums1[:m+n] = nums2[:n]
                return
            elif n == 0:
                return
            
            if nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1

# best
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p2 >= 0 and p1 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:  # nums2에 남은 요소 처리
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# nums1 = [2,0]
# m = 1
# nums2 = [1]
# n = 1

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5


sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)