// https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) -1
        
        while(low<=high):
            mid = int((low + high + 1)/2)
            # print(low, mid, high )
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                pass
        # print('-------------------')
        return -1