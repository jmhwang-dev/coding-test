# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def checkDepth(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
        
            depth_left = checkDepth(node.left)
            depth_right = checkDepth(node.right)
            if depth_left == 0:
                return depth_right + 1
            if depth_right == 0:
                return depth_left + 1
                
            return min(depth_left, depth_right) + 1
        return checkDepth(root)