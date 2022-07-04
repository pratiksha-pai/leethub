class Solution:
    def candy(self, a: List[int]) -> int:
        n=len(a)
        if n==1:
            return 1
        
        l=[1]*n
        r=[1]*n
        for i in range(1, n):
            if a[i] > a[i-1]:
                l[i]=l[i-1]+1
            if a[n-i-1] > a[n-i]:
                r[n-i-1]=r[n-i]+1

        s=0
        for i in range(n):
            s+=max(l[i],r[i])
        
        return s