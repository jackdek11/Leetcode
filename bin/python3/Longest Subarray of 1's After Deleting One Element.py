class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        count_zeros = 0
        left = 0

        for right, num in enumerate(nums):
            if num == 0:
                count_zeros += 1

            while count_zeros > 1:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1

            max_len = max(max_len, right - left)

        return max_len
