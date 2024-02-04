class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        
        R, C = len(mat), len(mat[0])
        
        res = 0
        memo = defaultdict(tuple)
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def dfs(x, y, prev):
            if x < 0 or y < 0 or x >= R or y >= C or mat[x][y] <= prev:
                return 0
            
            if (x, y) in memo:
                return memo[(x, y)]
            
            res = 1
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                res = max(res, 1 + dfs(nx, ny, mat[x][y]))
            
            memo[(x, y)] = res
            
            return memo[(x, y)]
        
        for x in range(R):
            for y in range(C):
                dfs(x, y, -1)
        
        return max(memo.values())
                
                