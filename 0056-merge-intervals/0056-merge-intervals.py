class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        intervals.sort()
        out.append(intervals[0])
        
        for interval in intervals[1:]:
            s, e  = interval
            if s > out[-1][1]:
                out.append([s, e])
            elif s>= out[-1][0] and e >= out[-1][1]:
                out[-1][1] = e
            elif e <= out[-1][1]:
                continue

        
        return out
                
            