class Solution:
    def findOrder(self, nc: int, prereq: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        g = defaultdict(list)
        degree = [0 for _ in range(nc)]
        
        for v, u in prereq:
            g[u].append(v)
            degree[v] += 1
        
        q = deque([i for i in range(len(degree)) if degree[i] == 0])
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            
            for v in g[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    q.append(v)
            
        if len(res) == nc:
            return res
        else:
            return []
        