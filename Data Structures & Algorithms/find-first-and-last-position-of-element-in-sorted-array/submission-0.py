class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def leftsearch(nums,target):
            l,r = 0,len(nums)-1

            while l<=r:
                mid = l+ (r-l)//2

                if nums[mid] == target:

                    if mid == 0:
                        return 0
                    
                    elif nums[mid]> nums[mid-1]:
                        return mid
                        
                    else:
                        r = mid-1
                
                elif nums[mid]>target:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        
        def rightsearch (nums,target):
            l,r = 0,len(nums)-1
            while l<=r:
                mid = l + (r-l)//2
                if nums[mid] == target:
                    if mid == len(nums)-1:
                        return mid

                    elif nums[mid] < nums[mid+1]:
                        return mid
                    
                    else:
                        l = mid+1
                elif nums[mid]<target:
                    l = mid+1
                else:
                    r = mid-1
            return -1


        left = leftsearch(nums,target)
        right = rightsearch(nums,target)

        return [left,right]