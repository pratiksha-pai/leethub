class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        return (nums[len(nums)-1]-1) * (nums[len(nums)-2]-1)