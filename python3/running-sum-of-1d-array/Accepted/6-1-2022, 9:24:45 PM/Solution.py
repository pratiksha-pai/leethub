// https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_array = 0
        sum_array = [0 for i in range(len(nums))] 
        total_sum = 0
        
        for i in range(len(nums)):
            total_sum = total_sum + nums[i]
            sum_array[i] = total_sum
            
        return sum_array