class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        alreadySeen = [False] * 10

        # Scan rows for duplicates
        for i in range(0, 9):
            alreadySeen = [False] * 10 
            for j in range(0, 9):
                if(board[i][j] != '.'):
                    if(alreadySeen[int(board[i][j])]):
                        return False
                    else:
                        alreadySeen[int(board[i][j])] = True
        
        # Scan columns for duplicates
        for i in range(0, 9):
            alreadySeen = [False] * 10 
            for j in range(0, 9):
                if(board[j][i] != '.'):
                    if(alreadySeen[int(board[j][i])]):
                        return False
                    else:
                        alreadySeen[int(board[j][i])] = True

        for boxRow in range(0, 9, 3):  # boxRow starts at 0, 3, 6 (top-left of each subbox)
            for boxCol in range(0, 9, 3):  # boxCol starts at 0, 3, 6 (top-left of each subbox)
                alreadySeen = [False] * 10  # Reset for each subbox
                for i in range(3):  # Iterate over rows of the subbox
                    for j in range(3):  # Iterate over columns of the subbox
                        num = board[boxRow + i][boxCol + j]
                        if num != '.':
                            num = int(num)
                            if alreadySeen[num]:
                                return False
                            else:
                                alreadySeen[num] = True
   
        return True
                  