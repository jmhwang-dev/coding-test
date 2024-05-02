class Solution:
    def isHappy(self, n: int) -> bool:
        check = []
        def checkHappy(n):
            if n == 1:
                return True
            if n in check:
                return False
            
            check.append(n)
            num = pow(n % 10, 2)
            quotient = n // 10
            while quotient >= 10:
                remainder = quotient % 10
                num += pow(remainder, 2)
                quotient = quotient // 10
            num += pow(quotient, 2)
            return checkHappy(num)
        return checkHappy(n)