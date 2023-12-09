class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_length = len(digits)
        
        i = digit_length - 1
        
        while digits[i] == 9 and i >= 0:
            i -= 1
        
        if i == -1:
            results = [0]*(digit_length + 1)
            results[0] = 1
            return results
        
        results = [0]*(digit_length)
        
        results[i] = digits[i] + 1
        
        for j in range(i-1, -1, -1):
            results[j] = digits[j]
        
        return results