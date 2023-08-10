class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = i
            else:
                return True
            
        return False