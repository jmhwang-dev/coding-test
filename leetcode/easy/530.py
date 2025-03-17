# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        sorted_values = sorted(values)
        mad = abs(sorted_values[0] - sorted_values[1])
        index = 1
        while index+1 < len(sorted_values):
            tmp = abs(sorted_values[index] - sorted_values[index+1])
            if tmp < mad:
                mad = tmp
            index+=1
        return mad