class Node:
    def __init__(self, val =0,next =None, prev =None,key = None):
        self.val,self.key = val,key
        self.prev,self.next = prev,next
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = 0
        self.capacity = capacity
        self.first = self.end = None
        self.div = {}
    def get(self, key: int) -> int:
        if key not in self.div:
            return -1
        else:
            node = self.div[key]
            self.remove(node)
            return self.div[key].val
    def remove(self,node):
        if node == self.first:
            return
        if node == self.end:
            self.end = node.prev
            if self.end:
                self.end.next = None
        else:
            if node.prev and node.next:
                node.prev.next,node.next.prev = node.next,node.prev
        if self.first:
            self.first.prev = node
        node.next = self.first 
        node.prev = None
        self.first = node
    def put(self, key: int, value: int) -> None:
        if self.cap == self.capacity and self.end and key not in self.div:
            k = self.end.key
            self.div.pop(k)
            self.end = self.end.prev
            if self.cap > 1:
                self.end.next = None
            else:
                self.first = self.end
            self.cap -= 1
        d = self.div
        if key not in d:
            d[key] = Node()
            self.cap += 1
        node = d[key]
        node.val,node.key= value,key
        if self.cap == 1:
            self.first = self.end = node
            return
        if self.first == node:
            return
        self.remove(node)