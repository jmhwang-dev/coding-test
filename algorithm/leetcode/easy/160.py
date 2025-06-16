# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 2: two pointer
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA = headA
        nodeB = headB

        while nodeA or nodeB:
            if not nodeA:
                nodeA = headB
            if not nodeB:
                nodeB = headA
            if nodeA == nodeB:
                return nodeA
            
            nodeA = nodeA.next
            nodeB = nodeB.next
        return 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1: hash table 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_table = {}
        for head_node in [headA, headB]:
            if not head_node:
                continue
            node = head_node
            while node:
                if not node in hash_table:
                    hash_table[node] = node.val
                else:
                    return node
                node = node.next
        return