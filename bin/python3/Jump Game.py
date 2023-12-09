class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        for i in range(1,len(nums)):
            if jump == 0:
                return False
            jump -= 1
            jump = max(jump,nums[i])
        return True
