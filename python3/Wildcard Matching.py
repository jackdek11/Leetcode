class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        
        dp[0][0] = True
        
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
                                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]
                    
        return dp[m][n]