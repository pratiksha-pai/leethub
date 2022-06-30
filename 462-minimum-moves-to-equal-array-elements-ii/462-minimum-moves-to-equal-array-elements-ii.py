class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        # find median and subtract
        n=len(nums)
        t=nums[int(n/2)]
        s=0
        for i in range(n):
            s+=abs(nums[i]-t)
        
        return s