class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good_integer = ""
        
        for i in range(len(num) - 2):
            substring = num[i:i+3]
            if len(set(substring)) == 1:
                if substring > max_good_integer:
                    max_good_integer = substring
        
        return max_good_integer