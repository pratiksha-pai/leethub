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
                if s[start:end] in wd and dfs(end):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False

        
        return dfs(0)