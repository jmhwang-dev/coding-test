from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) == 0:
            return result

        digit_map = {}
        start_ascii = 97
        for i in range(2, 10):
            incr = 3
            if i == 7 or i == 9:
                incr = 4
            letters = ''
            for ascii_num in range(start_ascii, start_ascii + incr):
                letters += chr(ascii_num)
            start_ascii += incr
            digit_map[str(i)] = letters

        def get_comb(index, digits, ans=''):
            if index == len(digits):
                return ans
            
            for char in digit_map[digits[index]]:
                output = ans + char
                output = get_comb(index+1, digits, output)
                if output:
                    result.append(output)

        get_comb(0, digits)
        return result


sol = Solution()

digits = "23"
result = sol.letterCombinations(digits)
print(result)