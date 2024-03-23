class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(n+1)]
        dp[0][0][0] = 1

        for i in range(1, n+1):
            # End with P, can be after any combination
            for A in range(2):
                for L in range(3):
                    dp[i][A][0] += dp[i-1][A][L]
                    dp[i][A][0] %= MOD

            # End with A, can only be once
            for L in range(3):
                dp[i][1][0] += dp[i-1][0][L]
                dp[i][1][0] %= MOD

            # End with L, L count can increase up to 2
            for A in range(2):
                for L in range(1, 3):
                    dp[i][A][L] = dp[i-1][A][L-1]
                    dp[i][A][L] %= MOD

        return sum(sum(row) for row in dp[n]) % MOD

    # # Example usage
    # print(checkRecord(2))  # 8
    # print(checkRecord(1))  # 3
    # print(checkRecord(10101))  # Expected large number
