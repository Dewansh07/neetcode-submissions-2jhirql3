class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])
        dp = [[0]* c for _ in range(r)]
        dp[0][0] = grid[0][0]

        for i in range(1,r):
            dp[i][0] = grid[i][0]+ dp[i-1][0]
        for i in range(1,c):
            dp[0][i] = grid[0][i]+ dp[0][i-1]

        for ro in range(1,r):
            for co in range(1,c):
                dp[ro][co] = grid[ro][co]+ min(dp[ro-1][co], dp[ro][co-1])
        return dp[r-1][c-1]
