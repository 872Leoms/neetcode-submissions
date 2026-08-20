class Solution:
    import heapq
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i in points:
            x,y = i
            dis = math.sqrt(((x)**2) + ((y)**2))
            if len(pq) < k:
                heapq.heappush(pq, (-dis,i))
            else:
                last = -pq[0][0]
                if dis < last:
                    heapq.heappop(pq)
                    heapq.heappush(pq,(-dis,i))
        res = []
        for i in pq:
            res.append(i[1])
        return(res)

