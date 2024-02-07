class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        x, y = [], []
        
        x = [poured]
        
        
        for i in range(query_row):
            y = [0 for _ in range(len(x) + 1)]
            for j in range(len(x)):
                overflow = max(x[j]-1.0, 0) / 2.0
                y[j] += overflow
                y[j+1] += overflow
            x = y
            
            
        return min(1, x[query_glass])
                