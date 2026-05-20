class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hSet = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in hSet:
                    return False
                hSet.add(board[i][j])
        
        for i in range(9):
            vSet = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in vSet:
                    return False
                vSet.add(board[j][i])

        for box_row in range(3):
            for box_col in range(3):
                boxSet = set()
                for i in range(3):
                    for j in range(3):
                        cell = board[box_row*3 + i][box_col*3 + j]
                        if cell == '.':
                            continue
                        if cell in boxSet:
                            return False
                        boxSet.add(cell)

        return True



        