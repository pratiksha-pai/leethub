class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def subsequenceIndex(source, target, start):
            si = ti = 0
            while si < len(source) and ti < len(target):
                if source[si] == target[ti]:
                    ti += 1
                si += 1
            return ti   

        count = 0
        i = 0
        while i < len(target):
            pos = subsequenceIndex(source, target[i:], 0)
            if pos == 0:
                return -1
            i += pos
            count += 1
        return count
    