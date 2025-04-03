from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = [ i for i in range(1, n+1) ]
        
        def get_comb(start, comb):
            if len(comb) == k:
                result.append(comb)
                return

            for i in range(start, len(nums)):
                get_comb(i+1, comb + [nums[i]])

        get_comb(0, [])

        return result


sol = Solution()
ans = sol.combine(4, 3)
print(ans)