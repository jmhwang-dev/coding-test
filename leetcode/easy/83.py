# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        current_node = head
        while current_node.next is not None:
            next_node = current_node.next
            if current_node.val != next_node.val:
                current_node = next_node
                next_node = next_node.next
            else:
                current_node.next = next_node.next
        return head