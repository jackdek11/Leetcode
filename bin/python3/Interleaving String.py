class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)  # Get lengths of all three strings
        if n1 + n2 != n3:  # If the lengths of s1 and s2 do not add up to the length of s3, return False
            return False
        
        # Create a boolean array to store the subproblem results
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        
        # If s1 and s2 are empty, and s3 is also empty, return True
        dp[0][0] = True
        
        # Fill the first row of dp
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        # Fill the first column of dp
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        # Fill the rest of the dp array
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                        (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        # Return the result for the final subproblem
        return dp[n1][n2]