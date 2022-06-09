// https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        visited = [[0 for i in range(n+1)] for j in range(n+1)] 
        
        for i in range(n+1):
            for j in range(n+1):
                if i==0 or j ==0:
                    continue
                elif i == 1 and j == 1:
                    visited[i][j] = 1 if not obstacleGrid[0][0] == 1 else 0
                else:
                    if obstacleGrid[i-1][j-1]  == 1:
                        visited[i][j] = 0
                    else:
                        visited[i][j] = visited[i-1][j] + visited[i][j-1]  
                        
        
        print(visited[n][n])
        return visited[n][n]
                
        
        