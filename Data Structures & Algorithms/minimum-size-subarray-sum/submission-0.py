class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if any(i>= target for i in nums):
            return 1

        min_c = float('inf')
        l = 0
        total = 0

        for r in range(len(nums)):
            total+=nums[r]

            while total>= target:
                min_c = min(min_c, (r-l+1))
                total-=nums[l]
                l+=1
        return min_c if min_c != float("inf") else 0
                