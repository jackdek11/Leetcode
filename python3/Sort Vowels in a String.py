class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        vowel_indices = []
        vowel_chars = []

        for i, char in enumerate(s):
            if char in vowels:
                vowel_indices.append(i)
                vowel_chars.append(char)

        vowel_chars.sort()

        result = list(s)

        for i, char in zip(vowel_indices, vowel_chars):
            result[i] = char

        return ''.join(result)
