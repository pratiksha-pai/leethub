class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        
        # left
        n = len(nums)
        l, r = 0, n-1
        
        
        while l <= r:
            mid = (l+r) //2
            if nums[mid] < t:
                l = mid + 1 
            elif nums[mid] > t: 
                r = mid - 1
            elif mid-1 >= 0  and nums[mid] == t and nums[mid] == nums[mid-1]:
                r = mid - 1
            elif nums[mid] == t:
                low = mid
                break
        
        if l > r:
            low = -1
        
        n = len(nums)
        l, r = 0, n-1
                
        while l <= r:
            mid = (l+r) //2
            if nums[mid] < t:
                l = mid + 1
            elif nums[mid] > t:  
                r = mid - 1
            elif mid + 1 <= n-1 and nums[mid] == t and nums[mid] == nums[mid+1]:
                l = mid + 1
            elif nums[mid] == t:
                high = mid
                break
                
        if l > r:
            high = -1
        
        return [low, high]