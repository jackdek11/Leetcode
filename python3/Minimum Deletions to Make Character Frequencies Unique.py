class Solution:
    def minDeletions(self, s: str) -> int:
        # Count the frequency of each character in the string
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Initialize a set to keep track of used frequencies
        used_freq = set()

        deletions = 0
        for char, count in freq.items():
            while count in used_freq:
                # If the same frequency is already used, decrement count
                count -= 1
                deletions += 1

            if count > 0:
                # Add the current frequency to used_freq
                used_freq.add(count)

        return deletions