memo = {}

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        global memo
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        elif n < 0:
            return 0
        memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return memo[n]