class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)  # Calculate the total sum of the array

        if total_sum < x:
            return -1  # If the total sum is less than x, it's impossible to reach x.

        if total_sum == x:
            return len(nums)  # If the total sum is already equal to x, no need to remove elements.

        target = total_sum - x  # The target sum we want to find in the array.

        left = 0
        current_sum = 0
        min_operations = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > target:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                min_operations = min(min_operations, len(nums) - (right - left + 1))
