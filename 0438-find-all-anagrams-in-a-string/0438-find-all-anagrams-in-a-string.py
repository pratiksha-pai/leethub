class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        m, n = len(s), len(p)
        if n > m:
            return []
        
        pmap = {}
        smap = {}
        res = []
        
        for k in range(26):
            pmap[ord('a') + k] = 0
            smap[ord('a') + k] = 0
        
        for i in range(n):
            pmap[ord(p[i])] += 1
            smap[ord(s[i])] += 1
        
        if smap == pmap:
            res.append(0)
        
        for i in range(n, m):
            sprev = ord(s[i - n])
            smap[sprev] -= 1
            smap[ord(s[i])] += 1
            if smap == pmap:
                res.append(i-n+1)
            
        return res 