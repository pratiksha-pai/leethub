class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n=len(s)
        def ispali(sub):
            return sub == sub[::-1]
        
        res = []
        def dfs(start, path):
            if start >= len(s):
                res.append(path)
                return 
            
            for end in range(start+1, len(s)+1):
                if ispali(s[start:end]):
                    dfs(end, path+[s[start:end]])
            
        
        dfs(0, [])
        
        return res
                    
        
        
                