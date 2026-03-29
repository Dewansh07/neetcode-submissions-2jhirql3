class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums)-1
        n = len(nums)

        while left<right:
            mid = (right+left)//2
            if nums[mid]>nums[right]:
                left = mid+1
            else:
                right = mid
        pivot = left
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (right+left)//2
            real_mid = (mid+pivot)%n
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1


