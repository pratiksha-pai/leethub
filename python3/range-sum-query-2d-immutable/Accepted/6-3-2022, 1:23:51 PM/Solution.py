// https://leetcode.com/problems/range-sum-query-2d-immutable

class NumMatrix:
    dp = [];

    def __init__(self, matrix: List[List[int]]):

        rows = len(matrix)
        cols = len(matrix[0])
        self.dp = [[0 for i in range(cols)] for j in range(rows)]
        
#         print('rows')
#         print(rows)
#         print('cols')
#         print(cols)
            
        # for i in range(0,rows):
        #     for j in range(0,cols):
        #         print(self.dp[i][j], end =" ")
        #     print()
        #     print('---------------------------')
                
        for i in range(0,rows):
            for j in range(0,cols):
                if i!=0:
                    self.dp[i][j] += self.dp[i-1][j]
                if j!=0:
                    self.dp[i][j] += self.dp[i][j-1]
                if i!=0 and j!=0:
                    self.dp[i][j] -= self.dp[i-1][j-1]
                
                self.dp[i][j] += matrix[i][j]
                
            #     print(self.dp[i][j], end =" ")
            # print()
            # print('--------------------')
            
            # for test in range(0, cols):
            #     if i!=0:
            #         print(self.dp[i-1][test], end =" ")
            

        
        # for i in range(0,rows):
        #     for j in range(0,cols):
        #         print(self.dp[i][j], end =" ")
        #     print()
        #     print('--------------------')
                    
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        temp = self.dp[row2][col2]
        
        if row1!=0:
            temp -= self.dp[row1-1][col2]
        if col1!=0:
            temp -= self.dp[row2][col1-1]
        if row1!=0 and col1!=0:
            temp += self.dp[row1-1][col1-1]
            

        return temp
            
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)