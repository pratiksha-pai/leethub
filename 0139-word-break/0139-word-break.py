class Solution:
    def wordBreak(self, s: str, wd: List[str]) -> bool:
        
        wd = set(wd)
        memo = {}
        
        def dfs(start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            for end in range(start+1, len(s)+1):
                segment = s[start:end]
                if segment in wd:
                    if dfs(end):
                        memo[start] = True
                        return True
            
            memo[start] = False
            return False
        
        return dfs(0)
                