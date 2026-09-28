class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dutch national flag time is N and space is 1

        n = len(nums)-1
        low = mid = 0
        high = n

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
                