class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        speed = r

        while l <= r:
            k = (l + r) // 2
            m = 0
            for p in piles:
                m += math.ceil(float(p) / k)
            if m <= h:
                r = k - 1
                speed = k
            else:
                l = k + 1
        return speed
        