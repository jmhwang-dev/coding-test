from typing import List
class Solution:
    def reverseWords(self, s: str) -> str:
        chars = s.split()
        print(chars)
        start = 0
        end = len(chars)-1
        
        while start != end and start <= end:
            if chars[start] == '':
                start += 1
                continue
            if chars[end] == '':
                end -= 1
                continue
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
        
        return ' '.join(chars)

sol = Solution()
output  = sol.reverseWords("a good   example")
print(output)
