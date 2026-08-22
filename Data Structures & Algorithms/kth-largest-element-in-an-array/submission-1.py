class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        pq = []
        for i in nums:
            if len(pq) == k and  i > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq,i)        
            elif len(pq) < k:
                heapq.heappush(pq,i)       
        return(pq[0])
