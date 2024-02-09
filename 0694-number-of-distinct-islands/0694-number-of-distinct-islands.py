class Solution:
    def numDistinctIslands(self, g: List[List[int]]) -> int:
        
        R, C = len(g), len(g[0])
        res = set()
        
        def dfs(x, y, direc):
            if x < 0 or y < 0 or x >= R or y >= C or g[x][y] == 0:
                return 
            g[x][y] = 0
            path.append(direc)
            dfs(x-1, y, 'l')
            dfs(x+1, y, 'r')
            dfs(x, y-1, 'u')
            dfs(x, y+1, 'd')
            path.append('b')
        
        for x in range(R):
            for y in range(C):
                if g[x][y] == 1:
                    path = []
                    dfs(x, y, 's')
                    res.add(tuple(path))
                        
        return len(res)
                        
            