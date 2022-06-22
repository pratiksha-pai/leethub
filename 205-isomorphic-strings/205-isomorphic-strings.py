class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        res={}
        for i in range(0, len(s)):
            if s[i] in res and res[s[i]]!=t[i]:
                return False
            elif s[i] not in res and t[i] in res.values():
                return False
            else:
                res[s[i]]=t[i]
            
            

        return True