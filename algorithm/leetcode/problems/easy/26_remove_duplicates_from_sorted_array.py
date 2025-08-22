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