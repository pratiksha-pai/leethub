// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        n = len(prices)
        if n==0: 
            return 0
        
        min_array = []
        max_array = []
        min_val = 10001
        max_val = 0
        res = 0
        
        for i in range(0,n):
            if prices[i] < min_val:
                min_val = prices[i]
                
            min_array.append(min_val) 

        for i in reversed(range(0,n)):
            if prices[i] > max_val:
                max_val = prices[i]
                
            max_array.append(max_val) 
        
        max_array = list(reversed(max_array))
        
#         for i in range(0,n):
#             print(min_array[i], end=' ')
        
#         print()
#         print('-----------')
        
#         for i in range(0,n):
#             print(max_array[i], end=' ')

        for i in range(0,n):
            if res < max_array[i] - min_array[i]:
                res = max_array[i] - min_array[i]
        
        
        
        return res
        
        
        
            
            
            
        