class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        t = 0
        for c in nums:
            if c:
                t = 0
            else:
                t += 1
                result += t
        return result