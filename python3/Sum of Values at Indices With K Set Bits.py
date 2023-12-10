class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            if self.countSetBits(i) == k:
                result += nums[i]
        return result

    @staticmethod
    def countSetBits(num):
        count = 0
        while num > 0:
            count += num & 1
            num >>= 1
        return count