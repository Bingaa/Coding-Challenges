#Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#1. Each row must contain the digits 1-9 without repetition.
#2. Each column must contain the digits 1-9 without repetition.
#3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowValid = [{'1','2','3','4','5','6','7','8','9'} for i in range(len(board))]
        colValid = [{'1','2','3','4','5','6','7','8','9'} for i in range(len(board))]
        squareValid = [{'1','2','3','4','5','6','7','8','9'} for i in range(len(board))]
        
        for i in range(len(board)): 
            for j in range(len(board[i])): 
                if board[i][j] != '.':
                    # check Rows 
                    if board[i][j] not in rowValid[i]: 
                        return False 
                    rowValid[i].remove(board[i][j])
                    # check Columns 
                    if board[i][j] not in colValid[j]: 
                        return False 
                    colValid[j].remove(board[i][j])
                    # check Square 
                    index = (i // 3) + 3*(j // 3)
                    if board[i][j] not in squareValid[index]: 
                        return False 
                    squareValid[index].remove(board[i][j])
        
        return True