class Solution:
    def scheduleCourse(self, c: List[List[int]]) -> int:
        
        n=len(c)
        ct=0 
        c=sorted(c, key = lambda x: x[1])
        i=0
        p=[]
        o=0
        while i<n:
            if ct+c[i][0] <= c[i][1]:
                ct+=c[i][0]
                p.append(c[i][0])
                p.sort(reverse=True)
                o+=1
            else:
                # print(c[i][0])
                if not ct==0 and c[i][0]<p[0] and ct-p[0]+c[i][0]<=c[i][1]:
                    ct+=c[i][0]-p[0]
                    del p[0]
                    p.append(c[i][0])
                    p.sort(reverse=True)
            i+=1
        return o