# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        c = None
        temp = None
        head = None
        for i in lists:
            if not temp:
                temp = i
            else:
                while temp and i:
                    if temp.val <= i.val:
                        if not c:
                            c = temp
                            head = c
                        else:
                            c.next = temp
                            c = c.next
                        temp = temp.next
                    else:
                        if not c:
                            c = i
                            head = c
                        else:
                            c.next = i
                            c = c.next
                        i = i.next
                c.next = temp or i
                temp = head
                c = None
        return temp

        