# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ext = head.next
        head.next = None
        while ext:
            before = head
            head = ext
            ext = head.next
            head.next = before
        return head
        