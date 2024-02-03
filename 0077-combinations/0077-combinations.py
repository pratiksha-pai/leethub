class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
            
        def backtrack(path, i):
            if len(path) == k:
                res.append(path[:])
                return
            
            for j in range(i+1, n):
                backtrack(path+[j+1], j)
        
        backtrack([], -1)
        
        return res
                    
                    