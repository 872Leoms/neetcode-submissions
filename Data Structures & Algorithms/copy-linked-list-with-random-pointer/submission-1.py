from _heapq import heapify
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        c = head
        def random(head):
            c = head
            while head:
                t = head.random
                head.next.random = t.next if t else None
                head = head.next.next
            return c
        def final(head):
            c = head.next
            while head:
                t = head.next
                head.next = None
                tn = t.next
                t.next = t.next.next if t.next else None
                head = tn
            return c
        while head:
            temp = Node(head.val,head.next)
            nextt = head.next
            head.next = temp
            head = nextt
        c = random(c)
        f = final(c)
        return(f)