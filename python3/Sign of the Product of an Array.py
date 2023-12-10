class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            if num == 0:
                return 0
            product *= num
        return 1 if product > 0 else -1