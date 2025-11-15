class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        init = nums[0]
        index_to_change = 1
        ans = 1
        
        for i, num in enumerate(nums[1:], 1):
            if num != init:
                nums[index_to_change] = num
                init = num
                ans += 1
                index_to_change += 1
        return ans

# latest ans
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return
        
        slow_index = 0
        for fast_index in range(1, len(nums)):
            if nums[slow_index] == nums[fast_index]:
                continue
            nums[slow_index+1] = nums[fast_index]
            slow_index += 1
        return slow_index + 1
                
            