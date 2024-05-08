class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = 1
        while numbers[start] + numbers[end] != target:
            if numbers[start] == numbers[end]:
                start = end + 1
                end = start + 1
                continue
            if end < len(numbers):
                end += 1
            if end == len(numbers):
                start += 1
                end = start + 1

        return [start+1, end+1]