class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k >= n // 2:
            # If k is large enough, we can do as many transactions as we want,
            # effectively making it equivalent to the "unlimited transactions" problem.
            return self.max_profit_unlimited_transactions(prices)

        # Initialize the buy and sell arrays.
        buy = [float('-inf')] * (k+1)
        sell = [0] * (k+1)

        # Perform the dynamic programming calculation.
        for i in range(n):
            for j in range(1, k+1):
                buy[j] = max(buy[j], sell[j-1] - prices[i])
                sell[j] = max(sell[j], buy[j] + prices[i])

        # Return the maximum profit after k transactions.
        return sell[k]

    @staticmethod
    def max_profit_unlimited_transactions(prices):
        """
        Calculates the maximum profit achievable with unlimited transactions.

        Args:
            prices (List[int]): List of stock prices.

        Returns:
            int: Maximum profit achievable.
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit