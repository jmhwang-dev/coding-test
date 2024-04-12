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