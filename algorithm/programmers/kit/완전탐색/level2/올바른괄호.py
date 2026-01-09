# stack
def solution(s):
    answer = True
    
    if s[0] == ")":
        return False
    
    stack = []
    for par in s:
        if par == '(':
            stack.append(par)
        
        else:
            if not stack:
                return False
            
            stack.pop()

    if len(stack) > 0:
        return False

    return True