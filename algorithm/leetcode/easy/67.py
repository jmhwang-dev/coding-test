class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a = int(a, 2)
        int_b = int(b, 2)
        int_ans = int_a + int_b
        return bin(int_ans)[2:]