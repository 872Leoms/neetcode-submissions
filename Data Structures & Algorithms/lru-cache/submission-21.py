class Node:
    def __init__(self, val =0,next =None, prev =None,key = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = 0
        self.capacity = capacity
        self.first = None
        self.end = None
        self.div = {}
    def get(self, key: int) -> int:
        if key not in self.div:
            return -1
        else:
            node = self.div[key]
            if node == self.end and self.cap > 1 and self.first:
                self.end = node.prev
                self.end.next = None
                node.prev = None
                node.next = self.first
                self.first.prev = node
                self.first = node
            if node != self.first and self.first and node.prev and node.next:
                node.prev.next,node.next.prev = node.next,node.prev
                node.next = self.first
                self.first.prev = node
                node.prev = None
                self.first = node
            print("get",self.first.val if self.first else None,self.end.val if self.end else None ,self.div)
            return self.div[key].val
    def put(self, key: int, value: int) -> None:
        if self.cap == self.capacity and self.end and key not in self.div:
            k = self.end.key
            self.div.pop(k)
            temp = self.end.prev
            if temp:
                temp.next = None
            self.end = temp
            if self.cap <= 1:
                self.first = self.end
            self.cap -= 1
        d = self.div
        if key not in d:
            d[key] = Node()
            self.cap += 1
        node = d[key]
        d[key].val = value
        d[key].key = key
        if self.cap == 1:
            self.first = node
            self.end = node
            print("we are here 1",self.div,key)
            return
        if self.first == node:
            print("we are in first",self.div,key)
            return 
        if self.end == node:
            self.end = node.prev
            self.end.next = None
            if self.end:
                self.end.next = None
            node.prev = None
        else:
            if node.prev and node.next:
                node.prev.next,node.next.prev = node.next,node.prev
        if self.first:
            self.first.prev = node
        node.next = self.first
        node.prev = None
        self.first = node
        print("put",key,self.first.val if self.first else None,self.end.val if self.end else None ,self.div)
