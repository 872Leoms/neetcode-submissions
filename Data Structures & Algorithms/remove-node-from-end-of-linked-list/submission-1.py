# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = head 
        length = 0
        while x:
            length += 1
            x = x.next
        d = head 
        a = head 
        temp = length - n + 1
        k = 1
        c = d
        while k < temp:
            c = d
            if not d.next:
                d = a
            else:
                d = d.next
            k += 1
        else:
            if c.next == d:
                c.next = d.next
            else:
                a = d.next
            return a


        