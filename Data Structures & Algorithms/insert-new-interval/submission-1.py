class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newlist = []
        newin = newInterval
        for i in intervals:
            if newin and i[1] >= newin[0] and i[0] <= newin[1]:
                    newin[0] = min(i[0],newin[0])
                    newin[1] = max(i[1],newin[1])
                    continue
            if newin and i[0] > newin[1]:
                     newlist.append(newin)
                     newin = 0
            newlist.append(i)
        if newin:
            newlist.append(newin)
        return(newlist)