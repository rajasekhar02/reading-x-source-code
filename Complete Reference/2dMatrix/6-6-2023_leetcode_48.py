from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        size = rows
        cycles = size // 2
        for i in range(0, cycles):
            # struggled at this logic
            # did not seperated the variables for row and col
            newSizeRow = size - i - 1
            newSizeCol = size - i - 1
            newSize = size - i * 2 - 1
            for rowEle in range(0, newSize):
                topLeft = [i, i + rowEle]
                topRight = [i + rowEle, newSizeCol]
                bottomRight = [newSizeRow, newSizeCol - rowEle]
                bottomLeft = [newSizeRow - rowEle, i]
                temp = matrix[topLeft[0]][topLeft[1]]
                matrix[topLeft[0]][topLeft[1]] = matrix[bottomLeft[0]][bottomLeft[1]]
                matrix[bottomLeft[0]][bottomLeft[1]] = matrix[bottomRight[0]][
                    bottomRight[1]
                ]
                matrix[bottomRight[0]][bottomRight[1]] = matrix[topRight[0]][
                    topRight[1]
                ]
                matrix[topRight[0]][topRight[1]] = temp
                # print(topLeft, topRight, bottomRight, bottomLeft)
            # print(topLeft, topRight, bottomLeft, bottomRight)


matrix = [[1, 2, 3] * 2, [4, 5, 6] * 2, [7, 8, 9] * 2] * 2
matrix2 = [[1, 2] * 2] * 4
Solution().rotate(matrix)
print(matrix)
