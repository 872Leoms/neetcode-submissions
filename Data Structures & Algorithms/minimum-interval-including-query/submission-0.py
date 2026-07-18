class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queue = []
        res = {}
        f = 0
        for i in sorted(queries):
            while  f < len(intervals) and intervals[f][0] <= i:
                s,e = intervals[f]
                heapq.heappush(queue,(e-s+1,e))
                f+=1
            while queue and queue[0][1] < i:
                heapq.heappop(queue)
            res[i] = queue[0][0] if queue else -1
        fres = []
        for i in queries:
            fres.append(res[i])
        return(fres)


        