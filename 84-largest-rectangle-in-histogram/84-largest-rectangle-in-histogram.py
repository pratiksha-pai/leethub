class Solution:
    def largestRectangleArea(self, a: List[int]) -> int:
        n=len(a)
        l=[]
        r=[]
        ls=[]
        ls.append(-1)
        rs=[]
        rs.append(n)
        # min_till_now
        for i in range(n):
            if i==0:
                l.append(i)
                ls.append(i)
                continue
            
            # check if the curr a[i] is bigger than the last max, then push it to the ls stack and update l 
            if ls[len(ls)-1]!=-1 and a[i]<=a[ls[len(ls)-1]]:
                while ls[len(ls)-1]!=-1 and a[i]<=a[ls[len(ls)-1]] :
                    ls.pop()
            
            l.append(ls[len(ls)-1]+1)
            ls.append(i)
            
            
        for i in reversed(range(n)):
            if i==n-1:
                r.append(n-1)
                rs.append(n-1)
                continue
            
            # check if the curr a[i] is bigger than the last max, then push it to the ls stack and update l 
            if rs[len(rs)-1]!=n and a[i]<=a[rs[len(rs)-1]]:
                while rs[len(rs)-1]!=n and a[i]<=a[rs[len(rs)-1]] :
                    rs.pop()
            
            r.append(rs[len(rs)-1]-1)
            rs.append(i)
            
        r.reverse()
        
        lrh=0
        # print(l)
        # print(r)
        # print(a)

        for i in range(n):
            temp=(r[i]-l[i]+1)*a[i]
            if lrh<temp:
                lrh=temp
        return lrh
            
                
                
            
            
            