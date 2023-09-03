class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import defaultdict
        
        if len(grid) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        visited = [[0 for _ in range(n)] for _ in range(m)]
        mp = defaultdict(list)
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def issafe(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            return True
        
        def explore(idx, x, y):
            if issafe(x, y) == False:
                return 
            
            if grid[x][y] == '0':
                return
            
            visited[x][y] = 1
            mp[idx].append((x, y))
            
            for i in range(4):
                new_x = x+dirs[i][0]
                new_y = y+dirs[i][1]
                if issafe(new_x, new_y) and visited[new_x][new_y]:
                    continue
                explore(idx, new_x, new_y)
        
        for x in range(m):
            for y in range(n):
                if visited[x][y] == 0 and grid[x][y] == '1':
                    idx = len(mp)
                    explore(idx, x, y)
        
        # print(mp)
    
        return len(mp)