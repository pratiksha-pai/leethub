class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_can_reach = 0
        n = len(nums)
        if n <= 1:
            return True
        dp = [False for _ in range(n)]
        dp[0] = True
        for i in range(n-1):
            # print(max_can_reach, nums[i]+i)
            for j in range(max_can_reach, min(nums[i]+i+1, n)):
                if dp[i] == True:
                    dp[j] = True
            max_can_reach = max(nums[i]+i, max_can_reach)
            
        # print(dp)
        return dp[n-1]