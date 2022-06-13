class Solution:
    def getmin(self, a:int, b:int)->int:
        if a<b: 
            return a
        return b
    
    def minimumTotal(self, t: List[List[int]]) -> int:
        n=len(t)
        if n==0:
            return 0
        if n==1:
            return t[0][0]
        
        for i in range(1,n):
            for j in range(0,i+1):
                if j==0:
                    t[i][j]+=t[i-1][j]
                    continue
                elif j==i:
                    t[i][j]+=t[i-1][j-1]
                    continue
                else:
                    t[i][j]+=self.getmin(t[i-1][j-1], t[i-1][j])
                
        mps=sys.maxsize
        
        for j in range(n):
            if mps>t[n-1][j]:
                mps=t[n-1][j]
        
        return mps
            
                
                
                
            