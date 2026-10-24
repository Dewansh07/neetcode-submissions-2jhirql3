class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = max(nums), sum(nums)

        def can_split(maxarr):
            currsum = 0
            subarr = 1
            for num in nums:
                if currsum+num>maxarr:
                    subarr+=1
                    currsum = num
                else:
                    currsum+= num
            return subarr<=k

        while l<r:
            mid = (l+r)//2

            if can_split(mid):
                r = mid
            else:
                l = mid+1
        return l