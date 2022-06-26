class Solution:
    def insert(self, a: List[List[int]], b: List[int]) -> List[List[int]]:
        
        n=len(a)
        # print(n)
        if len(a)==0:
            a.append(b)
            return a
        if len(b)==0:
            return a
        
        l=-1
        r=n
        
        a.append(b)
        a.sort(key=lambda t: t[0])
        # print(a)
        i=1
        while i<len(a):
            if a[i][0]<=a[i-1][1]:
                if a[i-1][1]<=a[i][1]:
                    a[i-1][1]=a[i][1]
                del a[i]
                # print(a)
            else:
                i+=1
            
        
        return a