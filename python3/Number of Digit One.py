class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        multiplier = 1  # Represents the current digit position

        while multiplier <= n:
            divider = multiplier * 10
            count += (n // divider) * multiplier + min(max(n % divider - multiplier + 1, 0), multiplier)
            multiplier *= 10

        return count