class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) -1
        
        while l <= h:
            mid = (l+h) // 2
            # print(nums[l], nums[mid], nums[h])
            if nums[mid] == target:
                return mid
            
            # searching for a targetusing binary search mainly depends on if the array is sorted or not, it does not work otherwise, hence we need to first check if l -> mid or mid -> h or sorted or not 
            # first check which part is sorted and then check if target is present inside or outside, handle l & h accordingly 
            # the logic here is to check for target in the sorted part, if not present keep eliminating the sorted parts until you get the one which has your target itms
            # l->mid is sorted
            if nums[l] <= nums[mid]:
                # check if the target is in the range of l and mid, no need of checking target <= nums[mid] since its already checked
                if nums[l] <= target < nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid -1
                    
                    
                    
        return -1
                