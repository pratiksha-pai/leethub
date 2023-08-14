class Solution:
    def jump(self, nums: List[int]) -> int:
        import sys
        max_from_here = 0
        n = len(nums)
        dp = [(2**53)-1 for _ in range(n)]
        dp[0] = 0
        for i in range(n):
            max_from_before = max_from_here
            max_from_here = max(max_from_here, nums[i]+i)
            for j in range(max(i+1, max_from_before), min(max_from_here+1, n)):
                dp[j] = min(1+dp[i], dp[j])
                
        return dp[n-1] 