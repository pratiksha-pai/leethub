class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        
        n = len(nums)
        res = set()
        if n == 0:
            return 0
        
        subs = [0] * n
        
        subs[0] = (nums[0] % p == 0) * 1
        for i in range(1, len(nums)):
            subs[i] = subs[i-1] + (nums[i] % p == 0) * 1
        
        for i in range(n):
            for j in range(i+1):
                curr = tuple(nums[j:i + 1])
                if subs[i] - (subs[j - 1] if j > 0 else 0) <= k:
                    res.add(curr)
        
        return len(res)
            