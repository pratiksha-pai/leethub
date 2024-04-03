class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [""]
        ans = 0
        for word in arr:
            for s in res:
                new_s = s + word
                if len(new_s) != len(set(new_s)):
                    continue 
                
                res.append(new_s)
                ans = max(ans, len(new_s))
        
        return ans