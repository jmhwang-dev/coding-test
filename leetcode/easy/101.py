# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True

        left_q = [root.left]
        right_q = [root.right]
        i = 0
        while i < len(left_q) and i < len(right_q):
            if not left_q[i] and not right_q[i]:
                i += 1
                continue
            if not left_q[i] or not right_q[i]:
                return False

            if left_q[i].val != right_q[i].val:
                return False
                
            left_q.append(left_q[i].left)
            left_q.append(left_q[i].right)

            right_q.append(right_q[i].right)
            right_q.append(right_q[i].left)

            i += 1
        
        return True