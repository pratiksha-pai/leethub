class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        if len(mat) == 0:
            return 0
        
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])
        
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                rows[i] += mat[i][j]

        for j in range(len(mat[0])):
            for i in range(len(mat)):
                cols[j] += mat[i][j]
                

        for i in range(len(rows)):
            for j in range(len(cols)):
                if rows[i] == 1 and cols[j] == 1 and mat[i][j] == 1:
                    res += 1
        
        return res
                    
            
            
            
                
        
                
                
                