class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0

        for i in nset:

            if i-1 not in nset:
                length = 1

                while i+length in nset:
                    length+=1

                longest = max(longest,length)
        return longest