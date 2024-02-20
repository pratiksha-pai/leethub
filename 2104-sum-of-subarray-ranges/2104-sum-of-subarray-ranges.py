class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            min_val, max_val = float('inf'), float('-inf')
            for j in range(i, len(nums)):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                res += max_val - min_val
        return res