class Solution:
    def maximumUnits(self, bt: List[List[int]], t: int) -> int:
        bt.sort(key=lambda x: -x[1])
        s=0
        l=0
        for i in range(len(bt)):
            a=bt[i][0]
            b=bt[i][1]
            if l+a<=t:
                l+=a
                s+=(a*b)
            else:
                s+=(t-l)*b
                return s
        return s