class Solution:
    def maximumUnits(self, bt: List[List[int]], t: int) -> int:
        bt.sort(key=lambda x: -x[1])
        s=0
        l=0
        for i in range(len(bt)):
            if l+bt[i][0]<=t:
                l+=bt[i][0]
                s+=(bt[i][0]*bt[i][1])
            else:
                s+=(t-l)*bt[i][1]
                return s
        return s