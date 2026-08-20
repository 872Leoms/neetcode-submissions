class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i in points:
            x,y = i
            dis = ((x)**2) + ((y)**2)
            heapq.heappush(pq, (-dis,i))
            if len(pq) > k:
                heapq.heappop(pq)
        res = []
        for i in pq:
            res.append(i[1])
        return(res)

