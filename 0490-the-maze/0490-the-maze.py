class Solution:
    def hasPath(self, maze: List[List[int]], src: List[int], dest: List[int]) -> bool:
        
        seen = set()
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def dfs(node):
            if node == dest:
                return True
            
            if tuple(node) in seen:
                return False
            
            
            seen.add(tuple(node))
            
            for dx, dy in dirs:
                x, y = node
                while 0 <= x+dx < len(maze) and 0 <= y+dy < len(maze[0]) and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                if dfs([x, y]):
                    return True
            return False
        
        return dfs(src)
            
            
            