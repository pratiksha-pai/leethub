class Solution:
    def minPartitions(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        c=0
        for i in range(n):
            # print(ord(s[i]))
            # print(ord("0"))
            t=(ord(s[i])-ord("0"))
            if c<t:
                  c=t
        return c