class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxSet = set()

        for i in range(9):
            for j in range(9):

                val = board[i][j]

                if val == '.':
                    continue
                
                row_key = (i, val)
                col_key = (val, j)
                box_key = (i//3, j//3, val)

                if row_key in boxSet or col_key in boxSet or box_key in boxSet:
                    return False
                
                boxSet.update([row_key, col_key, box_key])

        return True



        