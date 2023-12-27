class Solution:
    def reverse(self, x: int) -> int:
        
        neg = False        
        if x < 0:
            neg = True
            x = abs(x)
            
        res = []
        
        while x != 0:
            res.append(x%10)
            x = int(x/10)
        
        # print(res)
        
        ans = 0
        for y in res:
            ans = ans * 10 + y
        
        # print(ans) 
        # print(2**31)
        
        if neg:
            ans *= -1
        
        # print(ans) 
        
        if ans < - 2**31 or ans > 2**31 -1:
            ans = 0
        
        return ans
        
            
            