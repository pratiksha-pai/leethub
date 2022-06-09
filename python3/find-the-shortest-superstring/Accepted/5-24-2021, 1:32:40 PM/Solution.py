// https://leetcode.com/problems/find-the-shortest-superstring

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        @lru_cache(None)
        def connect(w1, w2):
            return [(w2[i:], len(w2) - i) for i in range(len(w1) + 1) if w1[-i:] == w2[:i] or not i][-1]
        
        N = len(words)
        dp = [[(float("inf"), -1)] * N for _ in range(1<<N)]
        for i in range(N): dp[1<<i][i] = (len(words[i]), -1)
            
        for mask in range(1<<N):
            n_z_bits = [j for j in range(N) if mask & 1<<j]
            for j, k in permutations(n_z_bits, 2):
                dp[mask][j] = min(dp[mask][j], (dp[mask ^ 1<<j][k][0] + connect(words[k], words[j])[1], k))
                
        mask = (1<<N) - 1
        prev = min(dp[mask])
        last = dp[mask].index(prev)
        prev = prev[1]
        ans = ""
        
        while prev != -1:
            ans = connect(words[prev], words[last])[0] + ans
            mask -= (1<<last)
            prev, last = dp[mask][prev][1], prev
            
        return words[last] + ans
        