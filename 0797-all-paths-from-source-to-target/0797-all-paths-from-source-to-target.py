class Solution:
    def allPathsSourceTarget(self, g: List[List[int]]) -> List[List[int]]:
        
        n = len(g)
        res = []
        q = deque([[0]])
        while q:
            path = q.popleft()
            node = path[-1]
            
            if node == n-1:
                res.append(path)
            
            for child in g[node]:
                q.append(path + [child])
        
        return res
            
            
                
                
            