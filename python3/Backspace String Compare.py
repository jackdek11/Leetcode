class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def typed_string(input_str):
            result = []
            for char in input_str:
                if char == '#':
                    if result:
                        result.pop()
                else:
                    result.append(char)
            return result

        return typed_string(s) == typed_string(t)