class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indices = []
        if s is None or len(s) == 0 or words is None or len(words) == 0:
            return indices
        wordCount = dict()
        for i in range(len(words)):
            if words[i] in wordCount:
                wordCount[words[i]] += 1
            else:
                wordCount[words[i]] = 1
        wordLength = len(words[0])
        wordArrayLength = wordLength * len(words)
        for i in range(0, len(s) - wordArrayLength + 1):
            current = s[i:i + wordArrayLength]
            wordMap = dict()
            index = 0
            j = 0
            while index < len(words):
                part = current[j: j + wordLength]
                if part in wordMap:
                    wordMap[part] += 1
                else:
                    wordMap[part] = 1
                j += wordLength
                index += 1
            if wordMap == wordCount:
                indices.append(i)
        return indices