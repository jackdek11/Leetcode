class Solution:
    def wordBreak(self, s, wordDict):
        def backtrack(start, path):
            if start == len(s):
                result.append(' '.join(path))
                return
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    backtrack(end, path + [word])
        
        wordSet = set(wordDict)
        result = []
        backtrack(0, [])
        return result
