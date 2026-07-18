class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            self.heap.append(val)
            self.heapfiyup(self.heap,len(self.heap)-1)
        else:
            if val > self.heap[0]:
                self.heap[0] = val
                self.heapfiydown(self.heap,0)
        return self.heap[0]
    def heapfiydown(self,heap,i):
        smallest = i
        left = (i * 2) + 1
        right = (i * 2) + 2
        if left < len(heap) and heap[smallest] > heap[left]:
            smallest = left
        if right < len(heap) and heap[smallest] > heap[right]:
            smallest = right 
        if smallest == i:
            return 
        else:
            heap[smallest],heap[i] = heap[i],heap[smallest]
            self.heapfiydown(heap,smallest)

    def heapfiyup(self,heap,i):
        if i == 0:
            return heap
        pa = (i - 1) // 2
        smallest = pa
        son = i
        if smallest < len(heap) and heap[smallest] > heap[son]:
            smallest = son
        if smallest == pa:
            return 
        heap[smallest],heap[pa] = heap[pa],heap[smallest]
        self.heapfiyup(heap,pa)

