class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        s = [nums[0]]
        
        for num in nums[1:]:
            if num > s[-1]:
                s.append(num)
            else:
                i = 0
                while num > s[i]:
                    i+=1
                s[i] = num
            
                
        return len(s)