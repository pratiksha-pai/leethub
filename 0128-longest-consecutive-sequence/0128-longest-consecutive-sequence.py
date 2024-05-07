class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in nums:
                curr = num 
                curr_streak = 1
                while curr + 1 in nums:
                    curr += 1
                    curr_streak += 1
                
                ans = max(curr_streak, ans)
        
        return ans
            
        