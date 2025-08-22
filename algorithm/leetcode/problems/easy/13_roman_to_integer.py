class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {}
        roman["I"] = 1
        roman["V"] = 5
        roman['X'] = 10
        roman['L'] = 50
        roman['C'] = 100
        roman['D'] = 500
        roman['M'] = 1000
        roman['IV'] = 4
        roman['IX'] = 9
        roman['XL'] = 40
        roman['XC'] = 90
        roman['CD'] = 400
        roman['CM'] = 900

        ans = 0
        start = 0
        while start < len(s):
            end = start+2
            if end <= len(s) and s[start:end] in roman:
                ans += roman[s[start:end]]
                start += 2
            else:
                ans += roman[s[start]]
                start += 1
        return ans