class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        newlist = [intervals[0]]
        for i in intervals:
            if i[1] >= newlist[-1][0] and i[0] <= newlist[-1][1]:
                newlist[-1][0] = min(i[0],newlist[-1][0])
                newlist[-1][1] = max(i[1],newlist[-1][1])
            else:
                newlist.append(i)
        return(newlist)

       