class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        start = 0
        end = len(nums) - 1
        
        if end < -1:
            return ans

        while start < end:
            while nums[start] != val:
                start += 1
                ans += 1
                if start == len(nums):
                    return ans
            while nums[end] == val:
                end -= 1
                if end < 0:
                    return ans

            if end < start:
                return ans

            tmp = nums[end]
            nums[end] = nums[start]
            nums[start] = tmp
            ans += 1

            start += 1
            end -= 1

        if start == end and nums[end] != val:
            ans += 1

        return ans
    
# ans2
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if len(nums) == 0:
            return 0

        comp_index = 0
        last_index = len(nums) - 1
        
        while comp_index < last_index:
            if nums[comp_index] != val:
                comp_index += 1
            else:
                nums[last_index], nums[comp_index] = \
                nums[comp_index], nums[last_index]
                last_index -= 1
        
        if comp_index == last_index:
            if nums[comp_index] != val:
                return comp_index + 1
            return comp_index


# best
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k