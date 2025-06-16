# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        ans = TreeNode(val=root.val, left=root.left, right=root.right)
        
        def dfs(node):
            if not node:
                return
            tmp = node.left
            node.left = node.right
            node.right = tmp

            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(ans)
        return ans