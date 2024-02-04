class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])
        
        start_x, start_y = -1, -1
        # walk over space 
        empty = 1 
        for x in range(R):
            for y in range(C):
                if grid[x][y] == 0:
                    empty += 1
                if grid[x][y] == 1:
                    start_x, start_y = x, y
        
        res = [0]
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dp = {}
        def dfs(x, y, remain):
            if x < 0 or y < 0 or x >= R or y >= C or grid[x][y] < 0: 
                return 
            if grid[x][y] == 2 and remain == 0:
                res[0] += 1
                return 
            if grid[x][y] == 2:
                return 
            
            temp, grid[x][y] = grid[x][y], -2
            
            for dx, dy in dirs:
                dfs(x+dx, y+dy, remain-1)
            
            grid[x][y] = temp
        
        dfs(start_x, start_y, empty)
        
        return res[0]
            
            
            
                    
                    