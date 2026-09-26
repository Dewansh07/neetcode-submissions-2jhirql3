class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''nums.sort()
        return nums[len(nums)//2]'''

        '''
        time = n log n cuz sorting
        space = o(n)
        '''

        count = 0
        cand = None
        for num in nums:
            if count == 0:
                cand = num
            if num == cand:
                count+=1
            else:
                count -=1
            
        return cand 

        # boyer moore time = O(n) space O(1)