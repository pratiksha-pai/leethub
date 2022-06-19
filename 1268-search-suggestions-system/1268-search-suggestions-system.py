class Solution:
    def suggestedProducts(self, p: List[str], s: str) -> List[List[str]]:
        
        if len(p)==0:
            return [[""]]
        if len(s)==0:
            return p
        
        res=[]
        
        p.sort()
        # print(p)

        for i in range(1,len(s)+1):
            temp=[]
            # print()
            # print(s[0:i])
            
            j=0
            while j<len(p):
                # print(p[j])
                if p[j].startswith(s[0:i]):
                    if len(temp)<3:
                        temp.append(p[j])
                    j+=1
                else:
                    del p[j]
                
            
            res.append(temp)
        
        # print(res)
        
        return res