class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        o = [0]*n

        zero = 0
        prod = 1

        for num in nums:
            if num == 0:
                zero+=1
            else:
                prod *= num

        if zero >1:
            return o
        
        elif zero ==1 :
            for i in range(n):
                if nums[i]!= 0:
                    continue
                else:
                    o[i] = prod
            return o
        else:
            left = 1
            for i in range(n):
                o[i] = left
                left*=nums[i]
            
            right = 1
            for i in range(n-1,-1,-1):
                o[i]*= right
                right *= nums[i]
            return o
