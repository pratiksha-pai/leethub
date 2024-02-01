class Solution:
    def search(self, nums: List[int], t: int) -> int:
        
        n = len(nums)
        l, r = 0, n-1
        
        while l<=r:
            mid = (l+r) // 2
            
            if nums[mid] == t:
                return mid
            elif nums[mid] < t:
                l = mid+1
            else:
                r = mid-1
        
        return -1
                