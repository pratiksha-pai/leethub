class Solution:
    def allPathsSourceTarget(self, g: List[List[int]]) -> List[List[int]]:
        
        n = len(g)
        res = []
        
        def dfs(node, path):
            if node == n-1:
                res.append(path.copy())
                return
            
            for child in g[node]:
                dfs(child, path + [child])
        
        
        
        dfs(0, [0])
        return res
            
            
                
                
            