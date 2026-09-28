class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        minh = []

        for num, freq in count.items():
            heapq.heappush(minh, (freq,num))

            if len(minh)> k:
                heapq.heappop(minh)
        return [num for freq,num in minh]