class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        roman_nums = {
            1 : 'I',
            5 : 'V',
            10 : 'X',
            50 : 'L',
            100 : 'C',
            500 : 'D',
            1000 : 'M'
        }

        sorted_roman_nums = dict(sorted(roman_nums.items(), reverse=True))

        start_num = num
        divide_by = 1000
        while start_num != 0:
            while start_num // divide_by == 0:
                divide_by = divide_by // 10

            num_start_with = start_num // divide_by
            target_num = num_start_with * divide_by

            if not num_start_with in [4, 9]:
                for key in sorted_roman_nums.keys():
                    if start_num - key >= 0:
                        tmp_result = sorted_roman_nums[key]
                        tmp_start_num = start_num - key
                        break
            else:
                target_symbol_num = (num_start_with + 1) * divide_by
                tmp_result = sorted_roman_nums[divide_by] + sorted_roman_nums[target_symbol_num]
                tmp_start_num = start_num - target_num

            if 0 < num_start_with and num_start_with < 4:
                result += sorted_roman_nums[divide_by] * num_start_with
                start_num = start_num - target_num
            else:
                result += tmp_result
                start_num = tmp_start_num

        return result
        


sol = Solution()

num = 3749
result = sol.intToRoman(num)
print()
print(result)
print(result == "MMMDCCXLIX")
print()

num = 5
result = sol.intToRoman(num)
print()
print(result)
print(result == "V")
print()

num = 58
result = sol.intToRoman(num)
print()
print(result)
print(result == "LVIII")