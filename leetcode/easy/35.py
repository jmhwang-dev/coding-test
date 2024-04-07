# 35. Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while True:
            middle = (end + start) // 2
            value = nums[middle]

            if middle == start:
                if nums[start] < target and target <= nums[end]:
                    return end
                elif target <= nums[start]:
                    return start
                elif nums[end] < target:
                    return end + 1

            if target == value:
                return middle
            elif target < value:
                end = middle
            elif target > value:
                start = middle