class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dp = [[False] * n for _ in range(m)]
        
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or dp[i][j] or board[i][j] != word[k]:
                return False
            dp[i][j] = True
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            dp[i][j] = False
            return res
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and not dp[i][j]:
                    if dfs(i, j, 0):
                        return True
        return False