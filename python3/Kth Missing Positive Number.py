class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_positives = []
        n = max(arr)
        arr_set = set(arr)
        for i in range(1, n + 1):
            if i not in arr_set:
                missing_positives.append(i)
        if not missing_positives:
            return arr[len(arr) - 1] + k
        if k > len(missing_positives):
            return arr[len(arr) - 1] + (k - len(missing_positives))
        return missing_positives[k - 1]