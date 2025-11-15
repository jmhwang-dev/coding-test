# ans1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        cnt_dict = {}
        for num in nums:
            if num in cnt_dict:
                cnt_dict[num] += 1
            else:
                cnt_dict[num] = 1
        
        max_val = 0
        max_key = 0
        for key, cnt in cnt_dict.items():
            if cnt > max_val:
                max_val = cnt
                max_key = key

        return max_key
    
# best
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate