class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        print(n)
        if n==0:
            return 0
        if n==1:
            return 1
        mp={}
        c=1
        l=0
        mp[s[0]]=0
        
        
        for r in range(1,n):
            if s[r] not in mp:
                mp[s[r]]=r
                if c<(r-l+1):
                    c=r-l+1
                continue
            if mp[s[r]]>=l:
                l=mp[s[r]]+1
            
            if c<(r-l+1):
                c=r-l+1

            mp[s[r]]=r
        
        if c<(r-l+1):
            c=r-l+1
        return c