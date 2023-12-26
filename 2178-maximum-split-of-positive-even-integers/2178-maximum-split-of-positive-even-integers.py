class Solution:
    def maximumEvenSplit(self, fs: int) -> List[int]:
        if fs % 2 != 0 or fs < 2:
            return []
        
        
        res = []
        curr = 0
        next_even = 2
        
        while curr + next_even <= fs:
            res.append(next_even)
            curr += next_even
            # print(res)
            next_even += 2
        
        if curr < fs:
            res[-1] += fs - curr
        
        return res