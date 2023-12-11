class Solution:
    def corpFlightBookings(self, bk: List[List[int]], n: int) -> List[int]:
        dp = [0] * n
        
        for i in range(len(bk)):
            u, v, w = bk[i][0], bk[i][1], bk[i][2]
            
            dp[u-1] += w
            if v < n:
                dp[v] -= w
        
        for i in range(1, n):
            dp[i]+= dp[i-1]
        
        return dp