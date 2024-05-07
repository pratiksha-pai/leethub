class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:
        
        res = []
        intervals.sort(key= lambda x:x[0])
        
        for i in range(len(intervals)):
            interval = intervals[i]
            if ni[1] < interval[0]:
                res.append(ni)
                return res + intervals[i:]
            elif ni[0] > interval[1]:
                res.append(interval)
            else:
                ni = [min(ni[0], interval[0]), max(ni[1], interval[1])]
        
        res.append(ni)
        return res