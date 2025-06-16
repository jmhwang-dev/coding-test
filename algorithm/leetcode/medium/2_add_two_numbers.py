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
    

# 두 번째 풀이
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_node = ListNode()
        tail_node = head_node

        cur_node1 = l1
        cur_node2 = l2

        while True:
            tail_node.val += cur_node1.val + cur_node2.val
            if tail_node.val >= 10:
                tail_node.val -= 10
                tail_node.next = ListNode(1)

            if cur_node1.next is None and cur_node2.next is None:
                return head_node
            
            if tail_node.next is None:
                tail_node.next = ListNode()
                
            tail_node = tail_node.next

            cur_node1 = ListNode() if cur_node1.next is None else cur_node1.next
            cur_node2 = ListNode() if cur_node2.next is None else cur_node2.next