class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            char_s, char_t = s[i], t[i]

            # Check if char_s already maps to a different char_t
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False

            # Check if char_t already maps to a different char_s
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False

            # Create the mappings
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True