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
        i=0
        while i+k<n:
            t+=(cp[i+k]-cp[i])
            
            if t<minsum:
                minsum=min(t, minsum)
            
            i+=1
        
        return sum(cp)-minsum