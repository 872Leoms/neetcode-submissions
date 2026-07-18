class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        last = intervals[0]
        res = 0
        for i in intervals[1:]:
            if i[0] < last[1]:
                last[1] = min(i[1],last[1])
                print("we are in")
                print(last,i)
                res += 1
            else:
                last = i
        return(res)
        