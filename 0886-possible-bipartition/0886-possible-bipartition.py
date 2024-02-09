class Solution:
    def possibleBipartition(self, n: int, dis: List[List[int]]) -> bool:
        from collections import defaultdict
        color = {}
        g = defaultdict(list)
        
        for u, v in dis:
            g[u].append(v)
            g[v].append(u)
        
        def bfs(i):
            if i in color:
                return True
            
            q = deque([i])
            color[i] = 0
            
            while q:
                u = q.popleft()
                for v in g[u]:
                    if v not in color:
                        color[v] = (1-color[u])
                        q.append(v)
                    elif color[v] == color[u]:
                        return False
                            
            return True
                
        for i in range(1, n+1):
            if i not in color and bfs(i) == False:
                return False
        
        return True