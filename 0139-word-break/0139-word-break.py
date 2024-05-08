class Solution:
    def wordBreak(self, s: str, wd: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        wd = set(wd)
        
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wd:
                    dp[i] = True
                    break
        
        return dp[n]