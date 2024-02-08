class Solution:
    def numDistinctIslands(self, g: List[List[int]]) -> int:
        
        R, C = len(g), len(g[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        
        def dfs(x, y, direction):
            if x < 0 or y < 0 or x >= R or y >= C or g[x][y] == 0:
                return
            path.append(direction)
            g[x][y] = 0
            dfs(x-1, y, 'l')
            dfs(x+1, y, 'r')
            dfs(x, y-1, 'u')
            dfs(x, y+1, 'd')
            path.append('b')
        
        ui = set()
        for i in range(R):
            for j in range(C):
                if g[i][j] == 1:
                    path = []
                    dfs(i, j, 's')
                    ui.add(tuple(path))
        
        return len(ui)
                