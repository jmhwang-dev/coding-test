class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        iter_cnt = k % len(nums)
        tmp = nums[-iter_cnt:]
        tmp += nums[:-iter_cnt]
        for i in range(len(nums)):
            nums[i] = tmp[i]