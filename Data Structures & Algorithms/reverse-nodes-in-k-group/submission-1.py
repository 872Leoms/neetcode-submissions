# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head,end):
            tend,thead = end,head
            prev = nex = None
            while head:
                nex = head.next
                head.next = prev
                prev = head
                head = nex
            print("head after reverse",tend.val,"end after",thead.val)
            return(tend,thead)
        def merge(end,start,secondend,secondstart):
            print(end.val,start.val,secondend.val if secondend else None ,secondstart.val if secondstart else None )
            if secondend:
                secondend.next = start
            if secondstart:
                end.next = secondstart
            else:
                end.next = None
        def main(head,k):
            beg = None
            start = None
            while head:
                end = head
                for i in range(k-1):
                    if end:
                        end = end.next
                    else:
                        return beg
                if end == None:
                    return beg
                secondstart = end.next
                secondend = start
                if secondend:
                    secondend.next = None
                end.next = None
                s,e = reverse(head,end)
                merge(e,s,secondend,secondstart)
                if not beg:
                    beg = s
                head = secondstart
                start = e
            return beg
        return main(head,k)
        