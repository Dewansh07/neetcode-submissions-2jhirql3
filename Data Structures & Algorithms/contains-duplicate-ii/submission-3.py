class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        se = set()
        n = len(nums)
        for i in range(n):
            if i>k:
                se.remove(nums[i-k-1])
            if nums[i] in se:
                return True
            se.add(nums[i])
        return False