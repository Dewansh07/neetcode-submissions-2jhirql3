class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        def reverse(l,r):
            while l<r:
                nums[l], nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        #REVERSE the whole array
        reverse(0,n-1)
        #reverse the k elemets from starting
        reverse(0,k-1)
        #reverse the rest of elements
        reverse(k,n-1)

