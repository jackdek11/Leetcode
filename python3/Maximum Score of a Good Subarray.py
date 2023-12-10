class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = [0] * n  # To store the leftmost index for each element
        right = [n - 1] * n  # To store the rightmost index for each element
        stack = []

        # Find the leftmost indices
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                right[stack.pop()] = i - 1
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)

        # Calculate the score for each subarray and find the maximum
        result = 0
        for i in range(n):
            if left[i] <= k <= right[i]:
                result = max(result, nums[i] * (right[i] - left[i] + 1))

        return result