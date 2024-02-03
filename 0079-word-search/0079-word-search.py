class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        n = len(word)
        R, C = len(board), len(board[0])
        visited = set()
        
        def dfs(i, x, y):
            if i == n:
                return True
            
            if x < 0 or y < 0 or x >= R or y >= C or board[x][y] != word[i] or (x, y) in visited:
                return False
            
            temp, board[x][y] = board[x][y], '#'
            
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if dfs(i+1, nx, ny):
                    return True
            
            board[x][y] = temp
            
            return False
        
        for i in range(R):
            for j in range(C):
                if dfs(0, i, j):
                    return True
        
        return False
            
        
        
                
            
        