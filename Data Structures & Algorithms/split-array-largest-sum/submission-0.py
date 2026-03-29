class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left,right = max(nums), sum(nums)

        def can_split(max_sum):
            subarr = 1
            currsum = 0
            for num in nums:
                if currsum+num> max_sum:
                    subarr+=1
                    currsum = num
                else:
                    currsum+=num
            return subarr <=k

        while left<right:
            mid = left+ (right-left)//2

            if can_split(mid):
                right = mid
            else:
                left = mid+1
        return left