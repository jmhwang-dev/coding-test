# 2
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = 0
        while index < len(haystack):
            if haystack[index:index+len(needle)] == needle:
                return index
            index += 1
        return -1

# 1
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)