class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points = sorted(points, key = lambda x: (-x[1], (x[1]-x[0])))
        # print(points)
        out = []
        out.append(points[0])
        
        def intersection(a, b):
            return [max(a[0], b[0]), min(a[1], b[1])]

        for i in range(1, len(points)):
            if points[i][1] < out[-1][0]:
                out.append(points[i])
                # out[-1][1] = points[i][0]
            else:
                # out.append(points[i])
                out[-1] = intersection(out[-1], points[i])
        # print(out)
        return len(out)