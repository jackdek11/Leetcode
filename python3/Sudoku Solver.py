class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.backtrack(board)
        
    def backtrack(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in '123456789':
                        if self.isPointValid(board, i, j, c):
                            board[i][j] = c
                            if self.backtrack(board): 
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    
    def isPointValid(self, board, x, y, c):
        for i in range(9):
            if board[i][y] == c:
                return False
            if board[x][i] == c:
                return False
            if board[3*(x//3)+i//3][3*(y//3)+i%3] == c:
                return False
        return True  