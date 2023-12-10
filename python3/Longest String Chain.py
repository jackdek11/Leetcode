class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort the words by length
        words.sort(key=len)

        # Create a dictionary to store the longest chain ending with each word
        word_chain = {}
        max_chain_length = 1

        for word in words:
            current_length = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in word_chain:
                    current_length = max(current_length, word_chain[prev_word] + 1)
            word_chain[word] = current_length
            max_chain_length = max(max_chain_length, current_length)

        return max_chain_length