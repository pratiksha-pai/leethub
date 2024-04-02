class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        sx, sy, ex, ey = 0, 0, len(mat)-1, len(mat[0])-1
        res = []
        while sx <= ex and sy <= ey:
            
            if sx<=ex:
                for y in range(sy, ey+1):
                    res.append(mat[sx][y])
                sx+=1
        
            if sy<=ey:
                for x in range(sx, ex+1):
                    res.append(mat[x][ey])
                ey-=1
            
            if sx<=ex:
                for y in range(ey, sy-1, -1):
                    res.append(mat[ex][y])
                ex-=1
            
            if sy<=ey:
                for x in range(ex, sx-1, -1):
                    res.append(mat[x][sy])
                sy+=1
                
                
        return res
            
            