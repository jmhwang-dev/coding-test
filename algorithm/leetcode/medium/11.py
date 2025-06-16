from typing import List 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        start_index = 0
        end_index = len(height) - 1

        while start_index < end_index:
            chosen_height = min(height[end_index], height[start_index])
            area = chosen_height * (end_index - start_index)
            result = max(area, result)

            if height[end_index] > height[start_index]:
                start_index += 1
            else:
                end_index -= 1
        return result

sol = Solution()

height = [1,8,6,2,5,4,8,3,7]
ans = 49
result = sol.maxArea(height)
print(result, result == ans)

height = [8,7,2,1]
ans = 7
result = sol.maxArea(height)
print(result, result == ans)