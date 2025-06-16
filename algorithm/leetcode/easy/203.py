# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        cur_node = head
        next_node = head.next
        while next_node is not None:
            if next_node.val == val:
                cur_node.next = next_node.next
                next_node = cur_node.next
            else:
                cur_node = cur_node.next
                next_node = next_node.next
        if head.val == val:
            return head.next
        else:
            return head