class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < len(nums) and nums[i] - 1 != i and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1 
        return len(nums) + 1