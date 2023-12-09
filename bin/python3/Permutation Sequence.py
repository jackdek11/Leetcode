class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        f, nums = [1], [0]
        for i in range(1, n + 1):
            f.append(f[i - 1] * i)
            nums.append(i)
        res = []
        for i in range(n - 1, -1, -1):
            idx = math.ceil(k / f[i])
            res.append(nums.pop(idx))
            k -= (idx - 1) * f[i]
        return ''.join(map(str, res))