from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = self.makeNumber(l1, 1)
        val2 = self.makeNumber(l2, 1)
        output = str(val1 + val2)

        head_node = ListNode()
        next_node = head_node
        for char in output[::-1]:
            node = ListNode(int(char))
            next_node.next = node
            next_node = node

        return head_node.next

    def makeNumber(self, node, ten):
        result = node.val * ten
        if node.next is None:
            return result
        return result + self.makeNumber(node.next, ten*10)