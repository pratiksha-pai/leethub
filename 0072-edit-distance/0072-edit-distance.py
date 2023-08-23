class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        
        dp = [[0 for _ in range(len(w1)+1)] for _ in range(len(w2)+1)]
        
        for i in range(0, len(w2)+1):
            for j in range(0, len(w1)+1):
                if i == 0 or j == 0:
                    dp[i][j] = i+j
                    continue
                
                if w1[j-1] != w2[i-1]:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                
        
        return dp[len(w2)][len(w1)]
        
        