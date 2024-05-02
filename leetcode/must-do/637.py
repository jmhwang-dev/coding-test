# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = [round(root.val, 5)]

        def bfs(parents):
            if len(parents) == 0:
                return
            children = []
            for parent in parents:
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)
            
            if len(children) == 0:
                return
            total_sum = 0
            for child in children:
                total_sum += child.val

            ans.append(round(total_sum/len(children), 5))
            bfs(children)
            
        bfs([root])
        return ans