class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(start, end):
            prev, curr = 0, 0
            for i in range(start, end):
                prev, curr = curr, max(prev + nums[i], curr)
            return curr

        if len(nums) == 1:
            return nums[0]
        return max(rob_range(0, len(nums) - 1), rob_range(1, len(nums)))