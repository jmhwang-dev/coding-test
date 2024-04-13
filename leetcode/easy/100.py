# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def createQueue(node):
    start = 0
    q = [node]
    while start < len(q):
        if q[start] is not None:
            q.append(q[start].left)
            q.append(q[start].right)
        start += 1
    return q
            
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = createQueue(p)
        queue_q = createQueue(q)
        
        if len(queue_p) != len(queue_q):
            return False
        
        for node1, node2 in zip(queue_p, queue_q):
            if node1 is None and node2 is None:
                continue
            elif node1 is not None and node2 is not None:
                if node1.val != node2.val:
                    return False
            else:
                return False
        return True