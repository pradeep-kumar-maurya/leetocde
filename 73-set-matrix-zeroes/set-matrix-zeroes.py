class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_with_zero = set()
        cols_with_zero = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows_with_zero.add(i)
                    cols_with_zero.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows_with_zero:
                    matrix[i][j] = 0
                if j in cols_with_zero:
                    matrix[i][j] = 0
