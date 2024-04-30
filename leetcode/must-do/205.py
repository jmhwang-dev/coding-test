class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_table = {}
        hash_table2 = {}
        for i in range(len(s)):
            hash_table[s[i]] = t[i]
            hash_table2[t[i]] = s[i]

        if len(hash_table) != len(hash_table2):
            return False
        
        tmp = ''
        for char in s:
            tmp += hash_table[char]

        return True if tmp == t else False