class Solution:
    def minPartitions(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
                
        return int(max(list(s)))