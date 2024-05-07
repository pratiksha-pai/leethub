class Solution:
    def minHeightShelves(self, books: List[List[int]], sw: int) -> int:
        n = len(books)
        dp = [0] + [float('inf') for _ in range(n)]

        for i in range(1, n+1):
            w, h, j = 0, 0, i-1
            while j >=0 and w+books[j][0] <= sw:
                w+=books[j][0]
                h = max(h, books[j][1])
                dp[i] = min(dp[i], h + dp[j])
                j-=1
        
        return dp[n]
                