class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        se= set(nums)

        return len(se)!=len(nums)