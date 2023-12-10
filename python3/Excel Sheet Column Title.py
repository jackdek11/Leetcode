class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            # Adjust columnNumber to be 0-based
            columnNumber -= 1
            # Calculate the remainder when dividing by 26 and convert it to a letter
            letter = chr(columnNumber % 26 + ord('A'))
            # Append the letter to the result
            result = letter + result
            # Update columnNumber for the next iteration
            columnNumber //= 26
        
        return result