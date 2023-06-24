class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowWise = [0] * 9
        colWise = [0] * 9
        blockWise = [0] * 9
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                twoPower = 1 << int(board[i][j])
                if rowWise[i] & twoPower:
                    return False
                if colWise[j] & twoPower:
                    return False
                # Key Logic Struggled With
                # blockRows = [0,1,2]
                # blockCols = [0,1,2]
                blockRow = i // 3
                blockCol = j // 3
                if blockWise[3 * blockRow + blockCol] & twoPower:
                    return False
                rowWise[i] |= twoPower
                colWise[j] |= twoPower
                blockWise[3 * blockRow + blockCol] |= twoPower
        return True
