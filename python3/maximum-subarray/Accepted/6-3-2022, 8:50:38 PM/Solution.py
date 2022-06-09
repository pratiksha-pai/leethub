// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = []
        n = len(nums)
        max_num = -10001
        
        if n==0:
            return 0
        
        res.append(nums[0])
        
        for i in range(1, n):
            temp = res[i-1] + nums[i]
            if temp < nums[i]:
                res.append(nums[i])
            else:
                res.append(temp)
                
        for i in range(0, n):
            if res[i] > max_num :
                max_num = res[i]
                
        return max_num
                
        