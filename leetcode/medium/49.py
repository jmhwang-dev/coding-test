from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        anagram_map = defaultdict(list)
        hash_map = {}
        curr_index = 0
        while curr_index < len(strs):
            curr_str = strs[curr_index]
            curr_str_list = list(curr_str)
            curr_str_list.sort()
            sorted_str = ''.join(curr_str_list)

            if sorted_str not in hash_map:
                hash_map[sorted_str] = [curr_str]
            else:
                hash_map[sorted_str].append(curr_str)

            curr_index += 1

        return list(hash_map.values())

strs = ["eat","tea","tan","ate","nat","bat"]
strs = [""]
strs = ["","b",""]
sol = Solution()
ans = sol.groupAnagrams(strs)
print(ans)        