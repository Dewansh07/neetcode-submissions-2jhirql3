"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(intervals, key = lambda x:x.start)
        ends = sorted(intervals, key =lambda x:x.end)
        
        s = 0
        e = 0

        rooms = 0
        max_rooms = 0

        while s<len(intervals):
            if starts[s].start<ends[e].end:
                rooms+=1
                max_rooms = max(max_rooms, rooms)
                s+=1
            else:
                rooms-=1
                e+=1
        return max_rooms
