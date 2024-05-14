class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        init_num = n
        while True:
            remainder = init_num % 2
            quotient = init_num // 2
            if quotient == 0:
                return ans + 1

            ans += remainder
            init_num = quotient