class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for y in range(n):
            dp[0][y] = grid[0][y] + (y!=0) * (dp[0][y-1])
        for x in range(m):
            dp[x][0] = grid[x][0] + (x != 0) * (dp[x-1][0])
            
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = grid[x][y] + min(dp[x-1][y], dp[x][y-1])
        
        return dp[m-1][n-1]