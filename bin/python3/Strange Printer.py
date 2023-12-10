class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = min(dp[i][k] + dp[k+1][j] for k in range(i, j))

        return dp[0][n-1]