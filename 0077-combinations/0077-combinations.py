class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        def dfs(path, idx):
            if len(path) == k:
                res.append(path[:])
            
            for i in range(idx+1, n+1):
                dfs(path + [i], i)
        
        dfs([], 0)
        return res
                