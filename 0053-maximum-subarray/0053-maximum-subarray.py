class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float('-inf')
        running_sum = 0 
        for x in nums:
            running_sum += x
            res = max(running_sum, res)
            if running_sum < 0:
                running_sum = 0
        
        return res 
            
        
