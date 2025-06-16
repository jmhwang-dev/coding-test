from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        
        start = 0
        while start < len(nums):
            if start == 0:
                if nums[start] > nums[start+1]:
                    return start
            if start == len(nums)-1:
                if nums[start-1] < nums[start]:
                    return start
            if nums[start-1] > nums[start]:
                start += 1
                continue
            if nums[start] < nums[start+1]:
                start += 1
                continue
            return start
            
sol = Solution()
nums = [1,2,3,1]
print(sol.findPeakElement(nums))
