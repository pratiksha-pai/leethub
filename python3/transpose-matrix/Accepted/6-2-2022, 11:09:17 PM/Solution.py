// https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows=len(matrix)
        cols=len(matrix[0])
        
        # new_rows = cols
        # new_cols = rows
        

        # new_matrix = [[None]*new_cols]*new_rows
        
        # for i in range(rows):
        #     for j in range(cols):
        #         print(new_matrix[j][i])
        
#         for i in range(rows):
#             for j in range(cols):
#                 new_matrix[j][i] = matrix[i][j]
#                 print(new_matrix[j][i])
        
#         print('----------------------------------')                
        new_matrix = []
        for i in range(cols):
            temp = []
            for j in range(rows):
                # print('i = ' + str(i) +  ' j = ' + str(j))
                temp.append(matrix[j][i])
                
            new_matrix.append(temp)
        
        return new_matrix
                
                
        