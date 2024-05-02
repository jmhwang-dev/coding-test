class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        s_index = 0
        t_index = 0
        while s_index < len(s):
            if t_index >= len(t):
                return False
            if s[s_index] != t[t_index]:
                t_index += 1
            else:
                s_index += 1
                t_index += 1
        return True