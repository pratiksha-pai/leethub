class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        def dfs(path,start):
            if len(path) == k:
                res.append(path[:])
                return 
            
            for i in range(start, n+1):
                dfs(path + [i], i+1)
        
        dfs([], 1)
        return res
                