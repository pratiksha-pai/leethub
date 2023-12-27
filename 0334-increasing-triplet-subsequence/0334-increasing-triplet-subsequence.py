class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n = len(nums)
        min_from_left = [0 for _ in range(n)]
        max_from_right = [0 for _ in range(n)]
        
        for i in range(n):
            if i == 0 :
                min_from_left[i] = nums[i]
                continue
            min_from_left[i] = min(min_from_left[i-1], nums[i])
        
        for i in range(n-1, -1, -1):
            if i == n-1:
                max_from_right[i] = nums[i]
                continue
            max_from_right[i] = max(max_from_right[i+1], nums[i])
        
        
        for i in range(n):
            if nums[i] > min_from_left[i] and nums[i] < max_from_right[i]:
                return True
        
        return False
                    