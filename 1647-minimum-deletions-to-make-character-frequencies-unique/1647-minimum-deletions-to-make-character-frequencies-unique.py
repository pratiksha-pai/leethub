class Solution:
    def minDeletions(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 0
        
        mp = {i : s.count(i) for i in set(s)}
        res=list(mp.values())
        res.sort(reverse=True)
        m=res[0]
        s=0
        for i in range(1,len(res)):
            if res[i-1]>res[i]:
                continue
            else:
                temps=res[i]-res[i-1]
                if res[i-1]!=0:
                    temps+=1
                res[i]-=temps
                s+=temps
        
        return s