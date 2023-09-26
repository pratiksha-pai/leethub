class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            res += ( (prices[i]-prices[i-1] > 0) * 1 ) * (prices[i]-prices[i-1])
        
        return res