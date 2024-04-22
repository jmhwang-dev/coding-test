# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur_node = head
        arr = {}
        while cur_node:
            if cur_node in arr:
                return True
            arr[cur_node] = 1
            cur_node = cur_node.next
        return False