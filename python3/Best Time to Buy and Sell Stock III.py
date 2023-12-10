class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        # forward traversal to calculate maximum profit from 0 to i
        max_profit_forward = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            max_profit_forward[i] = max(max_profit_forward[i - 1], prices[i] - min_price)
        
        # backward traversal to calculate maximum profit from i to n-1
        max_profit_backward = [0] * n
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit_backward[i] = max(max_profit_backward[i + 1], max_price - prices[i])
        
        # find the maximum profit from two transactions
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_profit_forward[i] + max_profit_backward[i])
        
        return max_profit