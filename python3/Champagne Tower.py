class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize the 2D array to represent glasses
        glasses = [[0.0] * (i + 1) for i in range(101)]
        glasses[0][0] = poured  # Pour champagne into the top glass

        # Simulate the overflow process
        for i in range(query_row):
            for j in range(i + 1):
                excess_champagne = max(0, (glasses[i][j] - 1) / 2)
                glasses[i + 1][j] += excess_champagne
                glasses[i + 1][j + 1] += excess_champagne

        # Ensure the value is between 0 and 1 (inclusive)
        return min(1.0, glasses[query_row][query_glass])