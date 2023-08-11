class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def permute(nums):
            result = [[]]
            
            for num in nums:
                new_subset = [s+[num] for s in result]
                result.extend(new_subset)
            return result
        
        return permute(nums)
        