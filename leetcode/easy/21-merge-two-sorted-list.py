# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode()
tail = head
class Solution(object):
    def __init__(self,):
        global head
        global tail

        head = ListNode()
        tail = head
        
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        global head
        global tail
        
        tmp = head.next
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next
        print('----')

        if list1 is None:
            tail.next = list2
            return head.next
        elif list2 is None:
            tail.next = list1
            return head.next

        node = ListNode()
        
        if list1.val <= list2.val:
            node.val = list1.val
            tail.next = node
            tail = node
            next1 = list1.next
            next2 = list2
        else:
            node.val = list2.val
            tail.next = node
            tail = node
            next1 = list1
            next2 = list2.next

        return self.mergeTwoLists(next1, next2)