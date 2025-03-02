class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        for char in s:
            if char.isdigit():
                stack.append(char)
            elif char in ['(', '+', '-']:
                stack.append(char)
            elif char == ')':
                tmp_str = ''
                while stack[-1] != '(':
                    tmp_str += stack.pop()
                    
                stack.pop()
                correct_str = tmp_str[::-1]
                num_result = self.calculate(correct_str)
                
                if num_result < 0:
                    if not stack:
                        stack.append('-')

                    elif stack[-1] == '-':
                        stack.pop()
                        stack.append('+')

                    elif stack[-1] == "+":
                        stack.pop()
                        stack.append('-')
                        
                    for c in str(num_result)[1:]:
                        stack.append(c)
                else:
                    if not stack:
                        pass

                    elif stack[-1] == '-':
                        stack.pop()
                        stack.append('-')

                    elif stack[-1] == "+":
                        stack.pop()
                        stack.append('+')

                    for c in str(num_result):
                        stack.append(c)

        result = 0
        num = 0
        i = 1
        for char in stack[::-1]:
            if char.isdigit():
                num += int(char) * i
                i *= 10
            else:
                if char == '-':
                    num *= -1
                result += num

                i = 1
                num = 0
        result += num

        return result
sol = Solution()

# input_s = "-1- 2"
# input_s = "11 - 11"
# input_s = "(1+(4+5+2)-3)+(6+8)"
# input_s = "1 + ((1 + 1) + 1)"
# input_s = "1-(     -2)"
# input_s = " 2-1 + 2 "
# input_s = "1-(2+3-(4+(5-(1-(2+4-(5+6))))))"

input_s = "(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))"
print(sol.calculate(input_s))