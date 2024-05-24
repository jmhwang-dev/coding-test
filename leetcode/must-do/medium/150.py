class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        goal = len(nums)-1
        while goal > 0:
            for i in range(goal-1, -1, -1):
                if goal <= nums[i] + i:
                    memo = i
            ans += 1
            goal = memo
        return ans
