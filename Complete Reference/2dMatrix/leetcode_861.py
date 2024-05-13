class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        """
            This solution arrives to the required answer by performing toggling columnwise
        """
        m = len(grid)
        n = len(grid[0])

        # Set score to summation of first column
        score = (1 << (n - 1)) * m

        # Loop over all other columns
        for j in range(1, n):
            count_same_bits = 0
            for i in range(m):
                # Count elements matching first in row
                if grid[i][j] == grid[i][0]:
                    count_same_bits += 1

            # Calculate score based on the number of same bits in a column
            count_same_bits = max(count_same_bits, m - count_same_bits)
            # Calculate the score contribution for the current column
            column_score = (1 << (n - j - 1)) * count_same_bits
            # Add contribution to score
            score += column_score

        return score
    def matrixScore2(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rowMaxDigit = rows
        colMaxDigit = (1 << cols) - 1
        # print(rowMaxDigit, colMaxDigit)
        for i in range(rows):
            rowNum = 0
            for j in range(cols):
                if grid[i][j] == 1:
                    rowNum |= (1 << (cols-j-1))
            toggleRow = rowNum ^ colMaxDigit
            if rowNum < toggleRow:
                for j in range(cols):
                    grid[i][j] ^= 1 
        
        for i in range(cols):
            colNum = 0
            for j in range(rows):
                if grid[j][i] == 1:
                    colNum += 1
            toggleCol = abs(colNum - rowMaxDigit)
            if colNum < toggleCol:
                for j in range(rows):
                    grid[j][i] ^= 1
        # print(grid)
        ans = 0
        for i in range(rows):
            rowNum = 0
            for j in range(cols):
                if grid[i][j] == 1:
                    rowNum |= (1 << (cols-j-1))
            ans += rowNum
        return ans
        
