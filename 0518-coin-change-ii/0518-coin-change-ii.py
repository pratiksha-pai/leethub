class Solution:
    def change(self, a: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for _ in range(a+1)]
        dp[0] = 1

        for j in range(n):
            for i in range(a+1):
                if i >= coins[j]:
                    dp[i] = dp[i]+dp[i-coins[j]]
        
        # print(dp)
        
        return dp[a]
            
            
            