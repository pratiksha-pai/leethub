class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return -1
        
        nums.insert(0, 0)
        
        for i in range(1,n+1):
            nums[i]+=nums[i-1]
        
        # print(nums)
        for i in range(1,len(nums)):
            if nums[i-1]==nums[-1]-nums[i]:
                # print(nums[i-1], nums[-1], nums[i])
                return i-1
        
        return -1