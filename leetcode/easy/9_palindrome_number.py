class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        rev_x = str_x[::-1]

        if len(str_x) != len(rev_x):
            return False
        
        if str_x != rev_x:
            return False
        
        return True