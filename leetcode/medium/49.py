from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        if len(strs) == 1:
            result.append(strs)
            return result
        
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

        for anagram in hash_map.values():
            result.append(anagram)

        return result

strs = ["eat","tea","tan","ate","nat","bat"]
strs = [""]
strs = ["","b",""]
sol = Solution()
ans = sol.groupAnagrams(strs)
print(ans)        