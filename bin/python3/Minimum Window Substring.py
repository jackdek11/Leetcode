from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        required = defaultdict(int)
        window = defaultdict(int)

        for char in t:
            required[char] += 1

        left = right = formed = 0
        required_count = len(required)
        min_window = float('inf')
        min_window_start = 0

        while right < len(s):
            char = s[right]
            window[char] += 1

            if char in required and window[char] == required[char]:
                formed += 1

            while formed == required_count and left <= right:
                char = s[left]

                if right - left + 1 < min_window:
                    min_window = right - left + 1
                    min_window_start = left

                window[char] -= 1

                if char in required and window[char] < required[char]:
                    formed -= 1

                left += 1

            right += 1

        if min_window == float('inf'):
            return ""
        else:
            return s[min_window_start:min_window_start + min_window]