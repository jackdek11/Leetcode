class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = {}
        for char in chars:
            char_count[char] = char_count.get(char, 0) + 1

        total_length = 0
        for word in words:
            word_count = {}
            valid_word = True

            for char in word:
                if char_count.get(char, 0) < word_count.get(char, 0) + 1:
                    valid_word = False
                    break
                word_count[char] = word_count.get(char, 0) + 1

            if valid_word:
                total_length += len(word)

        return total_length