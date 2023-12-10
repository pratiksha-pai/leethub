class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        if len(matrix) == 0:
            return [[]]
        
        out = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                out[j][i] = matrix[i][j]
                
        return out