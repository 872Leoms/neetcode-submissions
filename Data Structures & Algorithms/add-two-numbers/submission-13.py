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
            temp = r
            if x:
                temp += x.val
            if y:
                temp += y.val
            print(temp)
            if temp >= 10:
                x.val = temp % 10
            else:
                x.val = temp
            r = temp // 10
            d = x
            if x and not x.next and y and y.next:
                x.next = y.next
                x = x.next
                y = None
            elif x:
                x = x.next                
            if y:
                y = y.next
        else:
            if r > 0:
                l3 = ListNode()
                l3.val = r
                d.next = l3
        return l1
        