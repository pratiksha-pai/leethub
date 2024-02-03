class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        R, C = len(a), len(b)
        
        dp = [[0 for _ in range(C+1)] for _ in range(R+1)]
        
        for i in range(R+1):
            for j in range(C+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    continue
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if a[i-1] == b[j-1]:
                    dp[i][j] = max(dp[i][j], 1+dp[i-1][j-1])
        
        return dp[R][C]
                