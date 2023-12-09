class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(combination, start, k):
            if k == 0:
                combinations.append(combination)
                return

            for num in range(start, n + 1):
                backtrack(combination + [num], num + 1, k - 1)

        backtrack([], 1, k)
        return combinations