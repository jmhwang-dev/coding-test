from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = len(ratings)
        if len(ratings) == 1:
            return result
        
        if len(ratings) == 2:
            if ratings[0] != ratings[1]:
                return result + 1
            return result

        candies = [1 for _ in range(len(ratings))]
        curr_index = 0
        while curr_index < len(ratings) - 1:
            next_index = curr_index+1
            if ratings[curr_index] < ratings[next_index]:
                candies[next_index] = candies[curr_index] + 1

            elif ratings[curr_index] > ratings[next_index]:
                if candies[curr_index] <= candies[next_index]:
                    candies[curr_index] = candies[next_index] + 1
            curr_index += 1

        curr_index = -1
        last_index = len(ratings) * -1
        while last_index < curr_index:
            prev_index = curr_index - 1
            if ratings[prev_index] > ratings[curr_index]:
                if candies[prev_index] <= candies[curr_index]:
                    candies[prev_index] = candies[curr_index] + 1
            curr_index -= 1
        return sum(candies)
    
sol = Solution()
ratings = [1,6,10,8,7,3,2]
print(f"s {ratings}")
print(sol.candy(ratings))