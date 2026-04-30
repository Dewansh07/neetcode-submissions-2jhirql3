class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n ==0:
            return
        if n ==1:
            return nums[0]

        def solve(arr):
            n1 = len(arr)
            if n1 == 0:
                return

            if n1 ==1:
                return ar[0]

            dp = n1*[0]
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2,n1):
                dp[i] = max(dp[i-2]+arr[i], dp[i-1])
            return dp[-1]

        return max(solve(nums[1:]), solve(nums[:-1]))