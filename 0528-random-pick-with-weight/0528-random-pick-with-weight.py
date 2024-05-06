class Solution:

    def __init__(self, weights: List[int]):
        self.ps = []
        self.total = 0
        for w in weights:
            self.total += w
            self.ps.append(self.total)

    def pickIndex(self) -> int:
        t = random.random() * self.total
        l, h = 0, len(self.ps) - 1
        while l < h:
            m = (l+h) //2
            if self.ps[m] < t:
                l = m+1
            else:
                h = m
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()