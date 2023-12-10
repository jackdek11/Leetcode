class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        # dp[i][j] := max dot product of two subseqs nums[0..i) and nums2[0..j)
        dp = [[-math.inf] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j],
                                    max(0, dp[i][j]) + nums1[i] * nums2[j])

        return dp[m][n]