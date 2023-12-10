class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Pointers for s and t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move the pointer in s
            j += 1  # Always move the pointer in t

        return i == len(s)