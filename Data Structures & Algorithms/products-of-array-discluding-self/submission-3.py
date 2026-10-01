class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ar = [1]* len(nums)
        left = 1
        for i in range(len(nums)):
            ar[i]*= left
            left*= nums[i]

        right =1
        for i in range(len(nums)-1,-1,-1):
            ar[i]*= right
            right*=nums[i]
        return ar