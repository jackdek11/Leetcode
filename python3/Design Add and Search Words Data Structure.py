class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True
        

    def search(self, word: str) -> bool:
        return self.dfs(self.trie, word, 0)
        
    def dfs(self, node, word, i):
        if i == len(word):
            return '#' in node
        if word[i] == '.':
            for child in node:
                if child != '#' and self.dfs(node[child], word, i + 1):
                    return True
            return False
        
        if word[i] not in node:
            return False
        return self.dfs(node[word[i]], word, i + 1)