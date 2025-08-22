class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(s.split(' ')) != len(pattern):
            return False
        hash_table1 = {}
        hash_table2 = {}
        for char, p in zip(s.split(' '), pattern):
            if p not in hash_table1:
                hash_table1[p] = char
            elif hash_table1[p] != char:
                return False
            
            if char not in hash_table2:
                hash_table2[char] = p
            elif hash_table2[char] != p:
                return False

        if len(hash_table1) != len(hash_table2):
            return False
        
        for p, c in hash_table1.items():
            if hash_table2[c] != p:
                return False
        return True