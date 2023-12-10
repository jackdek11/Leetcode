class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def play(nums, left, right):
            if left > right:
                return 0
            
            score_left = nums[left] - play(nums, left+1, right)
            score_right = nums[right] - play(nums, left, right-1)
            
            return max(score_left, score_right)
        
        return play(nums, 0, len(nums) - 1) >= 0