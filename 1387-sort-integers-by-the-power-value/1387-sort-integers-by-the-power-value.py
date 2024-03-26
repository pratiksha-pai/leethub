class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def getPower(x):
            steps = 0
            while x != 1:
                steps += 1
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
            return steps

        power_list = [(i, getPower(i)) for i in range(lo, hi+1)]
        sorted_power_list = sorted(power_list, key=lambda x: (x[1], x[0]))
        return sorted_power_list[k-1][0]

        