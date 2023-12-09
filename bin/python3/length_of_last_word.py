class Solution:
    # 57ms
    def lengthOfLastWord(self, s: str) -> int:
        last_word = ""
        _ = s.split(" ")
        for i in reversed(range(len(_))):
            tmp = _[i]
            if tmp != "":
                return len(tmp)
        return len(s.split(" ")[-1])
