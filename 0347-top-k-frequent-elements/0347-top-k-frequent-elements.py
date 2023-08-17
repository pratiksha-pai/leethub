class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        n = len(nums)
        if n ==0:
            return []
        
        for i in range(n):
            if nums[i] not in mp:
                mp[nums[i]] = 1
            else:
                mp[nums[i]] += 1
        
        return  list(dict(sorted(mp.items(), key = lambda x: -x[1])))[:k]