from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 1
        unique_nums = set(nums)

        for num in unique_nums:
            if num - 1 not in unique_nums:
                cur_num = num
                cur_len = 1
                while cur_num + 1 in unique_nums:
                    cur_num += 1
                    cur_len += 1
                    ans = max(ans, cur_len)
        return ans
            

        
sol = Solution()
ans = sol.longestConsecutive([1,0,1,2])
print(ans)