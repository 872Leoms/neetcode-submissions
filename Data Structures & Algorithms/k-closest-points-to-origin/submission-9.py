class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def part(points,start,end):
            if start > len(points) - 1 or end < 0:
                return start
            poviot = start
            print(poviot)
            pvalue = (points[poviot][0]**2) + (points[poviot][1]**2)
            left = start
            points[start],points[end] = points[end],points[start]
            for i in range(start,end):
                dis = (points[i][0]**2) + (points[i][1]**2)
                if dis < pvalue:
                    points[i],points[left] = points[left],points[i]
                    left += 1
            points[left],points[end] = points[end],points[left]
            return left
        res = []
        left = 0
        right = len(points) - 1
        poviotind  = right 
        while True:
            poviotind = part(points,left,right)
            if poviotind == k :
                return points[:k]
            elif poviotind < k:
                left = poviotind + 1
            elif poviotind > k:
                right = poviotind - 1
        print(res)


        