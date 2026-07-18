# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x = list1
        y = list2
        c = None
        if not y:
            return list1
        elif not x:
            return list2
        if x.val < y.val:
            head = list1
        else:
            head = list2
        while x and y:
            if x.val >= y.val:
                c = y
                y = y.next
                if not y:
                    c.next = x
            else:
                if not c:
                    k = x.next
                    x.next = y
                    c = x
                    x = k
                else:
                    k = x.next
                    c.next = x
                    x.next = y
                    c = x
                    x = k
        return head
            
        