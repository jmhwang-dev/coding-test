class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        for char in s:
            if not char in hash_s:
                hash_s[char] = 1
            else:
                hash_s[char] += 1

        for char in t:
            if not char in hash_s:
                return False
            else:
                hash_s[char] -= 1
        
        for cnt in hash_s.values():
            if cnt != 0:
                return False

        return True