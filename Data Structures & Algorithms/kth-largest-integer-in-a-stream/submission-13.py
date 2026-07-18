class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n = sorted(nums)
        self.k = k
    def add(self, val: int) -> int:
        self.n.append(val)
        self.n.sort()
        self.nk = self.n[len(self.n) - self.k]
        return self.nk
