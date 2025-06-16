class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        start = 0
        end = len(nums) - 1
        
        if end < -1:
            return ans

        while start < end:
            while nums[start] != val:
                start += 1
                ans += 1
                if start == len(nums):
                    return ans
            while nums[end] == val:
                end -= 1
                if end < 0:
                    return ans

            if end < start:
                return ans

            tmp = nums[end]
            nums[end] = nums[start]
            nums[start] = tmp
            ans += 1

            start += 1
            end -= 1

        if start == end and nums[end] != val:
            ans += 1

        return ans