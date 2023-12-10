class Solution:
    # 74ms
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate(result, "", 0, 0, n)
        return result
    
    def generate(self, result: List[str], s: str, _open: int, close: int, n: int):
        if _open == n and close == n:
            result.append(s)
            return
        if _open < n:
            self.generate(result, s + "(", _open + 1, close, n)
        if close < _open:
            self.generate(result, s + ")", _open, close + 1, n)
