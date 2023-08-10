class Solution:
    def minEatingSpeed(self, piles: List[int], target: int) -> int:
        if target < len(piles):
            return -1
        
        def cal(m):
            s = 0 
            for i in range(len(piles)):
                s += (piles[i] + m-1 ) // m
            
            return s
        
        l = 1
        h = max(piles)
        
        while l <= h:
            m = (l+h) // 2
            
            res = cal(m)
            
            if res <= target:
                h = m - 1
            else:
                l = m + 1
        
        return l