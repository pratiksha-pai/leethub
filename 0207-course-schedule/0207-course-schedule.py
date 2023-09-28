class Solution:
    def canFinish(self, nc: int, ps: List[List[int]]) -> bool:
        if nc <= 1:
            return True
        
        n = len(ps)
        if n <=1:
            return True
        
        from collections import defaultdict
        mp = defaultdict(list)

        for i in range(n):
            mp[ps[i][0]].append(ps[i][1])

        def dfs(i, v, s):
            if s[i] == True:
                return False
            if v[i] == True:
                return True
            
            v[i] = True
            s[i] = True

            for l in mp[i]:
                if not dfs(l, v, s):
                    return False
            
            s[i] = False
            return True
        
        v = [False] * nc
        s = [False] * nc

        for i in range(nc):
            if not dfs(i, v, s):
                return False
        return True
        