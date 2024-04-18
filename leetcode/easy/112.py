# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(remain, cur_node):
            if not cur_node:
                return remain == 0
            if not cur_node.left and not cur_node.right:
                return remain - cur_node.val == 0
            left_ans = dfs(remain - cur_node.val, cur_node.left)
            if not cur_node.left:
                left_ans = False
            right_ans = dfs(remain - cur_node.val, cur_node.right)
            if not cur_node.right:
                right_ans = False
            return left_ans or right_ans

        if not root:
            return False
        if root.val == targetSum:
            if not root.left and not root.right:
                return True

        return dfs(targetSum, root)