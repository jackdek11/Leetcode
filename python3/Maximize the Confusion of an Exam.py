class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_consecutive = max_count = 0
        left = 0
        count = {}

        for right in range(len(answerKey)):
            count[answerKey[right]] = count.get(answerKey[right], 0) + 1
            max_count = max(max_count, count[answerKey[right]])

            if (right - left + 1) - max_count > k:
                count[answerKey[left]] -= 1
                left += 1

            max_consecutive = max(max_consecutive, right - left + 1)

        return max_consecutive