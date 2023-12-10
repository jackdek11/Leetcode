class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        myList = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                myList[i][j] = myList[i-1][j] + myList[i][j-1]
        return myList[-1][-1]