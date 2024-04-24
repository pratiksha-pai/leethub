class Solution:
    def tribonacci(self, n: int) -> int:
        x, y, z = 0, 1, 1
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 1
        else:
            for i in range(3, n+1):
                res = x + y + z
                x, y, z = y, z, res

            return res
                