class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        mp = {}
        
        for i in range(len(arr)):
            if arr[i] not in mp:
                mp[arr[i]] = 1
            else:
                mp[arr[i]] += 1
        
        for k, v in mp.items():
            if v > int(0.25 * len(arr)):
                return k
        return -1