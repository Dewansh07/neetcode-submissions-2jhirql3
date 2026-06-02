class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        se = set()

        for i in range(n):

            if len(se)>k:
                se.remove(nums[i-k-1])
            
            if nums[i] in se:
                return True
            se.add(nums[i])
        return False
