class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0

        ans = []
        while i<len(intervals) and intervals[i][1] < newInterval[0]:
            i+=1

        ans = intervals[:i]

        while i<len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1

        ans.append(newInterval)
        ans.extend(intervals[i:])
        return ans