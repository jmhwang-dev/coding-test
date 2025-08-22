# bad way. 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        start = 0
        ans = 0
        while start < len(s):
            hash_s = {s[start]:1}
            len_sub = 1
            end = start + 1
            while end < len(s) and s[end] not in hash_s:
                hash_s[s[end]] = 1
                len_sub += 1
                end += 1
            if len_sub > ans:
                ans = len_sub
            start += 1
        return ans