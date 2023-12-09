class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        prev_gray_code = self.grayCode(n - 1)
        gray_code = prev_gray_code + [2**(n-1) + num for num in reversed(prev_gray_code)]
        return gray_code