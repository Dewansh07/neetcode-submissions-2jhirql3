class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for x,y in points:
            sq_d = x**2+ y**2
            heapq.heappush(h, (-sq_d, [x,y]))

            if len(h)>k:
                heapq.heappop(h)
        return [point for vale, point in h]