class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [1] * len(nums)   
        def jump(index):
            if not memo[index]:
                return False
            if index >= len(nums):
                return False
            elif index == len(nums)-1:
                return True
            elif nums[index] == 0:
                if index == len(nums)-1:
                    return True
                else:
                    return False
            result = True
            for cur_index in range(nums[index]):
                next_index = nums[cur_index] + cur_index
                result = result or jump(next_index)
            memo[index] = result
        return jump(0)