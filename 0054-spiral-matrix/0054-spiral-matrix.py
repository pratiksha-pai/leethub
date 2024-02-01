class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        
        m, n = len(mat), len(mat[0])
        if m == 0 or n == 0:
            return [] 
        rs, re, cs, ce = 0, m-1, 0, n-1
        
        
        res = []
        
        while rs <= re and cs <= ce:
            
            for j in range(cs, ce+1):
                res.append(mat[rs][j])
            rs += 1

            for i in range(rs, re+1):
                res.append(mat[i][ce])
            ce -= 1
            
            if rs <= re:
                for j in range(ce, cs-1, -1):
                    res.append(mat[re][j])
                re -= 1
            
            if cs <= ce:
                for i in range(re, rs-1, -1):
                    res.append(mat[i][cs])
                cs += 1
        
        return res