"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not len(intervals):
            return 0
        intervals.sort(key= lambda x: x.start)
        prev = [intervals[0].end]
        room = 1
        for i in intervals[1:]:
            if i.start < min(prev):
                room += 1
                prev.append(i.end)
            else:
                 prev.remove(min(prev))
                 prev.append(i.end)
        return(len(prev))

        