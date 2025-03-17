class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]
        ans = []
        range_start = 0
        for range_end in range(1, len(nums)):
            if nums[range_end] - nums[range_end-1] != 1:
                if range_end-1 == range_start:
                    output = f"{nums[range_start]}"
                else:
                    output = f"{nums[range_start]}->{nums[range_end-1]}"
                ans.append(output)
                range_start = range_end

        if range_start == len(nums)-1:
            output = f"{nums[range_start]}"
        else:
            output = f"{nums[range_start]}->{nums[-1]}"
        ans.append(output)
        return ans