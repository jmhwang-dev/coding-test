# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def count(node):
            if node is not None:
                self.ans += 1
            else:
                return
            count(node.left)
            count(node.right)
        count(root)
        return self.ans