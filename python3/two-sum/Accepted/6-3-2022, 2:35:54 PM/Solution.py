// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = []
        res = []
        num1=None
        num2=None
        for i in range(len(nums)):
            new_nums.append(nums[i])
        
        
        new_nums.sort()
        left=0
        right=len(nums)-1
        while(left<right):
            
            if new_nums[right]+new_nums[left] == target:
                num1=new_nums[left]
                num2=new_nums[right]
                break
            elif new_nums[right]+new_nums[left] < target:
                left+=1
            else:
                right-=1
        
        for i in range(len(nums)):
            if nums[i] == num1 or nums[i]== num2:
                res.append(i)
        
        return res
            
                
            
        