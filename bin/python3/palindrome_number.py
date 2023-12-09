import math

class Solution:
    # 122ms
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
