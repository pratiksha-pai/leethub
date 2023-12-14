class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])
        
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
        
        for j in range(n):
            for i in range(m):
                cols[j] += grid[i][j]

        
        for i in range(m):
            for j in range(n):
                grid[i][j] = (rows[i] + cols[j]) * 2 - m - n
        
        
        return grid