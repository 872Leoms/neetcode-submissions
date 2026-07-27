# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        f,s = head,head
        def rev(p):
            if not p or not p.next:
                return p
            ex = p.next
            p.next = None
            while ex:
                before = p
                p = ex
                ex = p.next
                p.next = before
            return p
        while fast:
            prev = slow
            slow = slow.next
            if not fast.next:
                break
            fast = fast.next.next
        prev.next = None
        f = head
        s = rev(slow)
        i = f
        while f or s:
            t = f.next
            if s:
                i.next = s
                i = i.next
                s = s.next
            f = t
            if f: 
                i.next = f
                i = i.next


        