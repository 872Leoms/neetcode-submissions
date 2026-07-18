# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = l1
        y = l2
        d = None
        r = 0
        while x or y:
            l3 = ListNode()
            temp = r
            if x:
                temp += x.val
            if y:
                temp += y.val
            if temp >= 10:
                l3.val = temp % 10
                r = temp // 10
            else:
                l3.val = temp
                r = 0
            if not d:
                d = l3
                k = d
            else:
                d.next = l3
                d = d.next
            if x:
                x = x.next
            if y:
                y = y.next
        else:
            if r > 0:
                l3 = ListNode()
                l3.val = r
                d.next = l3
        return k
        