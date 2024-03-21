class Solution:
    def findMinDifference(self, time_points: List[str]) -> int:
        
        n = len(time_points)
        time_ints = []
        max_time = 24 * 60
        for time_str in time_points:
            hh = time_str.split(':')[0]
            mm = time_str.split(':')[1]
            time_ints.append(int(hh)*60 + int(mm))
        
        time_ints.sort()
        
        min_time = 24*60 + 1
        
        for i in range(1, n):
            diff = time_ints[i] - time_ints[i-1]
            min_time = min(min_time, diff)
        
        min_time = min(min_time, 24*60 - (time_ints[-1]- time_ints[0]))
        
        
        return min_time