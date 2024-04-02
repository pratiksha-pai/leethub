class Solution:
    def exist(self, b: List[List[str]], word: str) -> bool:
        

        n = len(word)
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def dfs(i, x, y):
            if i == n:
                return True
            
            if x < 0 or x >= R or y < 0 or y >= C or b[x][y] != word[i]:
                return False
            
            tmp, b[x][y] = b[x][y], '#'
            
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if dfs(i+1, nx, ny):
                    return True
            b[x][y] = tmp 
            
            return False
        
        R, C = len(b), len(b[0])
        
        for x in range(R):
            for y in range(C):
                if word[0] == b[x][y] and dfs(0, x, y):
                    return True
        
        return False
                