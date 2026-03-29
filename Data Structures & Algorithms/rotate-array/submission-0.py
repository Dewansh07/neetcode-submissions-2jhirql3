class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        if k ==0:
            return nums

        first = nums[-k:]
        for i in range(n-k-1,-1,-1):
            nums[i+k] = nums[i]
        nums[:k] = first

        