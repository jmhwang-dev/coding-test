from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        total_len = len(nums)
        ans = 1
        output = [1]
        for i in range(total_len):
            if i + 1 >= total_len:
                output.append(ans)
                break
            if sorted_nums[i+1] == sorted_nums[i]:
                continue
            if sorted_nums[i+1] - sorted_nums[i] == 1:
                ans += 1
            else:
                output.append(ans)
                ans = 1
        return max(output)

        
sol = Solution()
ans = sol.longestConsecutive([1,0,1,2])
print(ans)