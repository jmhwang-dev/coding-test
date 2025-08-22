class Solution:
    def mySqrt(self, x: int) -> int:
        curr_num = 0
        for i in range(0, 2147483648):
            pow_num = i*i
            if pow_num == x:
                return i
            elif pow_num < x:
                curr_num = i
            elif pow_num > x:
                break
        return curr_num