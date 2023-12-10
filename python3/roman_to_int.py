terms = {
    'I': 1, 
    'V': 5, 
    'X': 10, 
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000
}

class Solution:
    # 27ms runtime
    def romanToInt(self, s: str) -> int:
        result = 0
        try:
            for i, roman in enumerate(s):
                value = terms[roman]
                if value >= terms[s[i+1]]:
                    result += value
                else:
                    result -= value
        except Exception as e:
            result += value
        return result
"""
#  --------->> FIRST ATTEMPT <<---------
class Solution:
    # 121ms runtime
    def romanToInt(self, s: str) -> int:
        result = 0
        for i, roman in enumerate(s):
            value = terms[roman]
            try:
                if value >= terms[s[i+1]]:
                    result += value
                else:
                    result -= value
            except Exception as e:
                result += value
        return result
"""