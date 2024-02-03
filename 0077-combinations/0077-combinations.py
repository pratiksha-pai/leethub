class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
            
        def backtrack(path, start):
            if len(path) == k:
                res.append(path[:])
                return
            
            for j in range(start, n):
                backtrack(path+[j+1], j+1)
        
        backtrack([], 0)
        
        return res
                    
                    