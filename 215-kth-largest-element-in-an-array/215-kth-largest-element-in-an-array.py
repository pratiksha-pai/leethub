class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==0:
            return -1
        nums.sort()
        return nums[n-k]