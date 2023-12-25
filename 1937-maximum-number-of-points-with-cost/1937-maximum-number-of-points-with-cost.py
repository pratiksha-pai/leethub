class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        # at any point y you can look for max in the left part, max in the right part
        
        m, n = len(points), len(points[0])
        dp = points[0]
        
        for x in range(1, m):
            left = [0] * n
            right = [0] * n
            
            left[0] = dp[0]
            for y in range(1, n):
                left[y] = max(left[y-1]-1, dp[y])
                
            right[n-1] = dp[n-1]
            for y in reversed(range(n-1)):
                right[y] = max(right[y+1]-1, dp[y])
            
            for y in range(n):
                dp[y] = points[x][y] + max(left[y], right[y])
        
        
        return max(dp)