class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        R, C = len(a), len(b)
        
        dp = [[0 for _ in range(C+1)] for _ in range(R+1)]
        
        for i in range(1, R+1):
            for j in range(1, C+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if a[i-1] == b[j-1]:
                    dp[i][j] = max(dp[i][j], 1+dp[i-1][j-1])
        
        return dp[R][C]
                