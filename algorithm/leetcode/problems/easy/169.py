class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1
        
        appear = 0
        ans = 0
        for key, value in hash_table.items():
            if value > appear:
                ans = key
                appear = value
        return ans