// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        max_reps = 1
        max_reps_num = nums[0]
        curr_num = nums[0]
        n = len(nums)
        
        temp_max_reps = 0
        
        for i in range(1, n):
            if nums[i] != curr_num:
                
                if max_reps < temp_max_reps:
                    max_reps_num = curr_num
                    max_reps = temp_max_reps
                
                curr_num = nums[i]
                temp_max_reps = 1
            else:
                temp_max_reps += 1

        if max_reps < temp_max_reps:
            max_reps_num = curr_num
            max_reps = temp_max_reps

        return max_reps_num
                
            
            
        
        