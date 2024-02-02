class Solution:
    def allPathsSourceTarget(self, g: List[List[int]]) -> List[List[int]]:
        
        n = len(g)
        res = []
        visit = set()
        
        def dfs(node, path):
            if node == n-1:
                res.append(path.copy())
                return
            
            for child in g[node]:
                if child not in visit:
                    visit.add(child)
                    path.append(child)
                    dfs(child, path)
                    visit.remove(child)
                    path.pop()
        dfs(0, [0])
        return res
            
            
                
                
            