class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for i, num in enumerate(nums):
            if num not in hash_table:
                hash_table[num] = i
            else:
                if abs(hash_table[num] - i) <= k:
                    return True
                else:
                    hash_table[num] = i
        return False