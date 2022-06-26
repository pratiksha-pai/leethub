class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        # max count from cards on the sides = min count from cards in the middle 
        n=len(cp)
        if n==0:
            return 0
        if n<=k:
            return sum(cp)
        
        s=sum(cp)
        # print('sum is '+str(s))
        k=n-k
        # print(k)
        
        t=sum(cp[0:k])
        i=0
        minsum=t
        # print(t)
        # print(s-t)
        while i+k<n:
            # print('for i and i+k '+str(i)+' '+str(i+k))
            # print(t)
            # print(s-t)
            t+=cp[i+k]-cp[i]
            
            if t<minsum:
                # print('minsum')
                minsum=t
            
            i+=1
        
        return s-minsum