class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # 1. invert across the left to right diagonal 
        # 2. invert across the vertical axis
        
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        
        def swap_diag(x, y):
            # print(f'before {matrix[x][y]} and {matrix[y][x]}')
            t = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = t
            # print(f'after {matrix[x][y]} and {matrix[y][x]}')
            
        def swap_vert(x, y):
            # print(f'before {matrix[x][y]} and {matrix[y][x]}')
            t = matrix[x][y]
            matrix[x][y] = matrix[x][n-1-y]
            matrix[x][n-1-y] = t
            # print(f'after {matrix[x][y]} and {matrix[y][x]}')
        
        # 1 
        for x in range(m):
            for y in range(x+1, n):
                swap_diag(x, y)
                
        # 2 
        
        for x in range(m):
            for y in range(n//2):
                swap_vert(x, y)
        return