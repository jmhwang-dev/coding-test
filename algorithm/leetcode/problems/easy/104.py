# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root is None:
            return depth

        children = []
        for child in [root.left, root.right]:
            if child is not None:
                children.append(child)
        
        depth = 1
        start = 0
        cur_end = len(children)
        end = len(children)
        while start < end:
            if children[start].left:
                children.append(children[start].left)
                end += 1
            if children[start].right:
                children.append(children[start].right)
                end += 1

            start += 1
            if start == cur_end:
                start = cur_end
                cur_end = end
                depth += 1
        return depth