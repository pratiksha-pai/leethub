class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        # find median and subtract
        n=len(nums)
        t1=t2=0
        t1=nums[int(n/2)]
        # t2=nums[int(n/2)+1]
        s1=0
        for i in range(n):
            s1+=abs(nums[i]-t1)
            # s2+=abs(nums[i]-t2)
        
        return s1