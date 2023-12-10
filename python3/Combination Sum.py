class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        length = len(candidates)
        def traverse(comb, start_index):
            if sum(comb) == target:
                output.append(comb[:])
                return
            if sum(comb) > target:
                return
            for index in range(start_index, length):
                comb.append(candidates[index])
                traverse(comb, index)
                comb.pop()
        traverse([], 0)
        return output