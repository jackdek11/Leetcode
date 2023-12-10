class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0  # Initialize the index for non-zero elements

        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != 0:
                # Move non-zero elements to the current non_zero_index
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1