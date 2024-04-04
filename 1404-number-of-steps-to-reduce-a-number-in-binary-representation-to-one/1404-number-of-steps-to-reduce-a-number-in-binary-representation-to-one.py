class Solution:
    def numSteps(self, s: str) -> int:
        
        ans = 0
        num = int(s, 2)
        
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            ans += 1
        return ans