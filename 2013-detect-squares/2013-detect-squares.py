class DetectSquares:

    def __init__(self):
        self.points = set()
        self.pcount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.add(tuple(point))
        self.pcount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        count = 0
        for x, y in self.points:
            if px!= x and abs(px-x) == abs(py-y):
                count += self.pcount[(px, y)] * self.pcount[(x, py)] * self.pcount[(x, y)]
        
        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)