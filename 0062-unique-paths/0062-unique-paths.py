class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for x in range(m):
            dp[x][0] = 1
        for y in range(n):
            dp[0][y] = 1
        
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x-1][y] + dp[x][y-1]
        print(dp)
        return dp[m-1][n-1]