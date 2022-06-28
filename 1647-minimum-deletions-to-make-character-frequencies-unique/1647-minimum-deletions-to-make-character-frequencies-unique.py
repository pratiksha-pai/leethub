class Solution:
    def minDeletions(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 0
        mp={}
        for i in range(n):
            if s[i] not in mp:
                mp[s[i]]=1
            else:
                mp[s[i]]+=1
        res=[]
        mp=sorted(mp.items(), key=lambda item: item[1], reverse=True)
        for i in range(len(mp)):
            res.append(mp[i][1])
        
        # print(mp)
        # print(res)
        
        m=res[0]
        s=0
        for i in range(1,len(res)):
            # print('for i '+str(i))
            if m>res[i]:
                # print('in if')
                m=res[i]
            else:
                # print('in else')
                if m==0:
                    temps=res[i]
                else:
                    temps=(res[i]-m+1)
                res[i]-=temps
                # print(res)
                # print(temps)
                s+=temps
                m=res[i]
                
        
        return s