class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if any(i>= target for i in nums):
            return 1
        minn = float('inf')
        total = 0
        l = 0

        for r in range(len(nums)):
            total+=nums[r]

            while total>=target:
                minn = min(minn, r-l+1)
                total-=nums[l]
                l+=1
        return minn if minn != float('inf') else 0
                