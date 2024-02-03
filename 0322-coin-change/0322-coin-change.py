class Solution:
    def coinChange(self, coins: List[int], a: int) -> int:
        
        dp = [2**31 for _ in range(a+1)]
        dp[0] = 0
        
        for i in range(1, len(coins) + 1):
            for j in range(1, a+1):
                if j >= coins[i-1]:
                    dp[j] = min(dp[j], 1 + dp[j-coins[i-1]])
        
        ans = dp[a]
        return ans if ans <= (2**31 - 1) else -1
            
            
        
        