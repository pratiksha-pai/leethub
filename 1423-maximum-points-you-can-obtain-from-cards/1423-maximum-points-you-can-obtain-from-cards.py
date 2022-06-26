class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        # max count from cards on the sides = min count from cards in the middle 
        n=len(cp)
        if n==0:
            return 0
        if n<=k:
            return sum(cp)
        
        k=n-k
        minsum=t=sum(cp[0:k])
        
        for i in range(0, n-k):
            t+=(cp[i+k]-cp[i])
            
            if t<minsum:
                minsum=t
        
        return sum(cp)-minsum