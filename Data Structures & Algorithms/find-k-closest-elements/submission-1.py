class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minheap = []

        for num in arr:
            heapq.heappush(minheap, (abs(num-x),num))

        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        res.sort()

        return res