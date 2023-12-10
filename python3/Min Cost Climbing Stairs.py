class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Initialize dp array with cost values
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        
        # Calculate minimum cost to reach each step
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # The minimum cost to reach the top is the minimum of the last two steps
        return min(dp[-1], dp[-2])