# 2: OMG...
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits

# 1
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        total_sum = 0
        digit_count = len(digits) - 1
        for digit in digits:
            total_sum += digit * pow(10, digit_count)
            digit_count -= 1
        total_sum += 1

        rev_ans = []
        while total_sum != 0:
            remainder = total_sum % 10
            quotient = total_sum // 10
            rev_ans.append(remainder)
            total_sum = quotient
        return rev_ans[::-1]