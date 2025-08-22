class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        paren = []
        for p in s:
            if len(paren) == 0:
                paren.append(p)
            elif paren[-1] == '(' and p == ')':
                paren.pop()
            elif paren[-1] == '{' and p == '}':
                paren.pop()
            elif paren[-1] == '[' and p == ']':
                paren.pop()
            else:
                paren.append(p)
        if len(paren) != 0:
            return False
        return True
