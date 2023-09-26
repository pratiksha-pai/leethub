class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        m = len(s1)
        n = len(s2)
        o = len(s3)
        
        if o != m+n:
            return False
        
        if m ==0:
            return s2 == s3
        if n ==0 :
            return s1 == s3
        
        dp = [[False for _ in range(n+1)] for _ in range(m+1)] # s1 = left wall, s2 ceiling
        dp[0][0] = True # null and null make null
        
        for i in range(m+1):
            for j in range(n+1):
                # print(i, j)
                if i==0 or j == 0:
                    if i == j:
                        continue
                    
                    if i == 0:
                        dp[i][j] = (dp[i][j-1] and s3[i+j-1] == s2[j-1])
                    else:
                        dp[i][j] = (dp[i-1][j] and s3[i+j-1] ==  s1[i-1]) # yuck
                    continue
                   
                dp[i][j] = (dp[i][j-1] and (s3[i+j-1] == s2[j-1])) or (dp[i-1][j] and (s3[i+j-1] == s1[i-1]))
        
        # print(dp)
        
        return dp[m][n]