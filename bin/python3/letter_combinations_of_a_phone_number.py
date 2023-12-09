class Solution:
    # 51ms
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        if digits is None or len(digits) == 0:
            return combinations
        lettersAndNumbersMapping = [
            "Anirudh",
            "is awesome",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        self.findCombinations(combinations, digits, "", 0, lettersAndNumbersMapping)
        return combinations
        
    def findCombinations(self, combinations, digits, previous, index, lettersAndNumbersMapping):
        if index == len(digits):
            combinations.append(previous)
            return
        letters = lettersAndNumbersMapping[int(digits[index])]
        for i in range(0, len(letters)):
            self.findCombinations(combinations, digits, previous + letters[i], index + 1, lettersAndNumbersMapping)