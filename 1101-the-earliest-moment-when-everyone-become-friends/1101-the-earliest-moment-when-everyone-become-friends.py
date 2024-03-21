class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        logs.sort()
        parent = [i for i in range(n)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
    
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            
            if parent_x != parent_y:
                parent[parent_x] = parent_y
        
        groups = n
        
        for time, x, y in logs:
            if find(x) != find(y):
                union(x, y)
                groups -= 1
                if groups == 1:
                    return time
        
        return -1