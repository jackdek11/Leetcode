class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_freq = {}  # Dictionary to store the frequency of each number
        good_pairs = 0

        # Count the frequency of each number in the array
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1

        # Calculate the number of good pairs for each number
        for freq in num_freq.values():
            if freq > 1:
                good_pairs += (freq * (freq - 1)) // 2

        return good_pairs