class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h_table = {}
        for char in magazine:
            if char in h_table:
                h_table[char] += 1
            else:
                h_table[char] = 1

        for char in ransomNote:
            if char not in h_table:
                return False
            else:
                if h_table[char] == 0:
                    return False
                else:
                    h_table[char] -= 1
        return True
