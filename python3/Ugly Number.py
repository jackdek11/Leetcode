class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: # Non-positive numbers are not ugly
            return False
        while n % 2 == 0: # Check if n is divisible by 2, keep dividing until it's not
            n /= 2
        while n % 3 == 0: # Check if n is divisible by 3, keep dividing until it's not
            n /= 3
        while n % 5 == 0: # Check if n is divisible by 5, keep dividing until it's not
            n /= 5
        return n == 1 # If n is not 1, then it's not an ugly number
