class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        curr_line = []
        curr_width = 0
        for word in words:
            if curr_width + len(curr_line) + len(word) > maxWidth:
                num_spaces = maxWidth - curr_width
                if len(curr_line) == 1:
                    result.append(curr_line[0] + ' ' * num_spaces)
                else:
                    num_gaps = len(curr_line) - 1
                    even_spaces = num_spaces // num_gaps
                    extra_spaces = num_spaces % num_gaps
                    justified_line = ''
                    for i in range(num_gaps):
                        if i < extra_spaces:
                            justified_line += curr_line[i] + ' ' * (even_spaces + 1)
                        else:
                            justified_line += curr_line[i] + ' ' * even_spaces
                    justified_line += curr_line[-1]
                    result.append(justified_line)
                curr_line = []
                curr_width = 0
            curr_line.append(word)
            curr_width += len(word)
        last_line = ' '.join(curr_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        return result