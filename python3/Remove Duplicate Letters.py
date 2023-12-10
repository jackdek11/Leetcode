class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()  # To keep track of characters in the stack
        last_occurrence = {}  # To keep track of the last occurrence index of each character

        # Populate the last_occurrence dictionary
        for i, char in enumerate(s):
            last_occurrence[char] = i

        for i, char in enumerate(s):
            if char not in seen:
                # Pop characters from the stack if they are greater than the current character
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)

        return ''.join(stack)