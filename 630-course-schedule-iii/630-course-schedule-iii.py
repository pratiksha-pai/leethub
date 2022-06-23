class Solution:
    def scheduleCourse(self, c: List[List[int]]) -> int:
        q = []
        heapq.heapify(q)
        n=len(c)
        ct=0 
        c=sorted(c, key = lambda x: x[1])
        i=0
        o=0
        # print(c)
        while i<n:
            # print(c[i][0])
            if ct+c[i][0] <= c[i][1]:
                ct+=c[i][0]
                q.append(-1*c[i][0])
                o+=1
            else:
                heapq.heapify(q)
                if ct!=0 and len(q)!=0:
                    h=q[0]
                    if c[i][0]<-1*h and ct+h+c[i][0]<=c[i][1]:
                        ct+=(c[i][0]+h)
                        del q[0]
                        q.append(-1*c[i][0])

            # print(q)
            i+=1
        return o