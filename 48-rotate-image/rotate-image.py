class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(0, rows, 1):
            for j in range(i + 1, cols, 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for row in range(0, rows, 1):
            i, j = 0, cols - 1
            while i < j:
                temp = matrix[row][j]
                matrix[row][j] = matrix[row][i]
                matrix[row][i] = temp
                i += 1
                j -= 1
