class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n = len(nums)
        first_small = float('inf')
        second_small = float('inf')
        
        
        for num in nums:
            if num <= first_small:
                first_small = num
            elif num <= second_small:
                second_small = num
            else:
                return True
        
        return False
                    