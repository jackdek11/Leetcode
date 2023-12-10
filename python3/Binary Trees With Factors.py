class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        
        dp = [1] * n  # Initialize dp array with 1, as each element can form a tree by itself

        index = {num: i for i, num in enumerate(arr)}  # Create a mapping of numbers to their indices

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:  # Check if arr[j] is a factor of arr[i]
                    factor = arr[i] // arr[j]
                    if factor in index:  # Check if the other factor is present in the array
                        dp[i] = (dp[i] + dp[j] * dp[index[factor]]) % MOD

        return sum(dp) % MOD