"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        s,e = 0,0
        maxr, r = 0,0

        while s<len(intervals):
            if starts[s] < ends[e]:
                r+=1
                maxr = max(maxr, r)
                s+=1
            else:
                r-=1
                e+=1
        return maxr