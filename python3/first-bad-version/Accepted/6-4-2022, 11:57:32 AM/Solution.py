// https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    bad_version = 1
    
    def firstBadVersion(self, n: int) -> int:
        low = 1;
        high  = n;
        
        while(low<=high):
            mid = int((low+high)/2)
            if(isBadVersion(mid) == True):
                self.bad_version = mid
                high = mid -1
            else:
                low = mid+1
        
        return self.bad_version