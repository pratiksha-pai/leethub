// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        i=1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i+=1
            