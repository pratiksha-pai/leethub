class Solution:
    def exist(self, b: List[List[str]], word: str) -> bool:
        

        n = len(word)
        # seen = set()
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def dfs(path, i, x, y):
            if i == n:
                if ''.join(path) == word:
                    return True
                else:
                    return False
            
            
            if 0<=x<R and 0<=y<C and b[x][y] == word[i] and (x, y) not in seen:
                seen.add((x, y))
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if dfs(path + [word[i]], i+1, nx, ny):
                        return True
                seen.remove((x, y))
            
            return False
        
        R, C = len(b), len(b[0])
        
        for x in range(R):
            for y in range(C):
                if word[0] == b[x][y]:
                    seen = set()
                    if dfs([], 0, x, y):
                        return True
        
        return False
                