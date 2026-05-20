class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prev_e = float('-inf')
        count = 0

        for s,e in intervals:
            if prev_e <= s:
                prev_e = e
            else:
                count+=1
        return count