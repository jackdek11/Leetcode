class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        # Reverse each word in the list
        reversed_words = [word[::-1] for word in words]
        
        # Join the reversed words with spaces to form the result
        return ' '.join(reversed_words)