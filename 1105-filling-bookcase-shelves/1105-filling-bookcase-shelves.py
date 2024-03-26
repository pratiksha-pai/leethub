class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0] + [float('inf')] * len(books)
        for i in range(1, len(books) + 1):
            width, height, j = 0, 0, i
            while j > 0 and width + books[j - 1][0] <= shelfWidth:
                width += books[j - 1][0]
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)
                j -= 1
        return dp[-1]