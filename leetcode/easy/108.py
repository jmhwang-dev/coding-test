# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(val=nums[0])
        if len(nums) == 2:
            node = TreeNode(val=nums[0])
            node.right = TreeNode(val=nums[1])
            return node
        
        index = len(nums) // 2
        mid = TreeNode(val=nums[index])
        mid.left = self.sortedArrayToBST(nums[:index])
        mid.right = self.sortedArrayToBST(nums[index+1:])
        return mid        