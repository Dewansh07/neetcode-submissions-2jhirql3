class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]

        dp[0][0] = 1
        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(1,m):
            if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1:
                dp[i][0] = 1

        for j in range(1,n):
            if obstacleGrid[0][j] == 0 and dp[0][j-1] ==1:
                dp[0][j] = 1

        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c] ==0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[-1][-1]


