class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        mp = defaultdict(list)
        
        m, n = len(grid), len(grid[0])
        total_non_rotten = 0
        total_rotten = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    total_rotten += 1
                    mp[0].append((i, j))
                elif grid[i][j] == 1:
                     total_non_rotten += 1
        
        def issafe(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            return True
        
        def bfs(t):
            all_nodes = mp[t]
            
            for (x, y) in all_nodes:
                for dx, dy in [[-1,0], [1,0], [0, 1], [0, -1]]:
                    nx, ny = x+dx, y+dy
                    
                    if issafe(nx, ny) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        mp[t+1].append((nx, ny))
        
            if t+1 not in mp:
                return
            bfs(t+1)
        
        bfs(0)
        
        total_covered = 0
        
        for k, v in mp.items():
            total_covered += len(v)
        print(total_covered)
        
        
        return len(mp) - 1 if total_non_rotten + total_rotten == total_covered else -1