class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        import math
        r = math.gcd(p, q)
        p = int(p/r)
        q = int(q/r)
        # print(r)
        # print(p, q)
        
        if p%2==1 and q%2==0:
            return 0
        elif p%2==0 and q%2==1:
            return 2
        else:
            return 1