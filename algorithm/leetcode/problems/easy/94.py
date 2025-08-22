# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def DFS(ans, node):
    if node is None:
        return
    
    DFS(ans, node.left)
    ans.append(node.val)
    DFS(ans, node.right)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        DFS(ans, root)
        return ans