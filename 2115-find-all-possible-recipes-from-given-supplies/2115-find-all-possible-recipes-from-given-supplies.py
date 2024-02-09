class Solution:
    def findAllRecipes(self, recps: List[str], ings: List[List[str]], sups: List[str]) -> List[str]:
        
        from collections import defaultdict
        g = defaultdict(list)
        degree = defaultdict(int)
        sups = set(sups)
        res = set()
        
        for rec, ing_list in zip(recps, ings):
            for ing in ing_list:
                if ing not in sups:
                    g[ing].append(rec)
                    degree[rec] += 1
        
        q = deque([rec for rec in recps if degree[rec] == 0]) 
        
        while q:
            u = q.popleft()
            res.add(u)
            
            for v in g[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    q.append(v)
        
        return [rec for rec in recps if rec in res]