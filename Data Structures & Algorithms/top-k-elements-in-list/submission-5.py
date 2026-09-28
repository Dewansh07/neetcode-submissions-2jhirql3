class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min heap gives time= NlogK and space is K
        '''count = Counter(nums)

        minh = []

        for num, freq in count.items():
            heapq.heappush(minh, (freq,num))

            if len(minh)> k:
                heapq.heappop(minh)
        return [num for freq,num in minh]'''

        # now we do bucket sort which can do time in O(N) space is N
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for num,freq in count.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res