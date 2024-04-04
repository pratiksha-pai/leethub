class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b, ans = s.count('a'), 0, len(s)
        for c in s:
            if c == 'b':
                ans = min(ans, a + b)
                b += 1
            else:
                a -= 1
        return min(ans, b)