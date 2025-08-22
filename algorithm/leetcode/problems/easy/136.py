# 2 bit manipulation ...
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums[1:]:
            ans = ans ^ num
        return ans

# 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        arr = {}
        for num in nums:
            if num not in arr:
                arr[num] = 1
            else:
                arr[num] += 1

        for key, val in arr.items():
            if val == 1:
                return key
