class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        The idea is to iterate over the matrix and find the rows and columns where matrix[row][col] == 0.
        We will add rows to a set and also add columns to a set wherever row and column is pointing to 0.
        """
        rows_with_zero = set()
        cols_with_zero = set()

        # iterate over the matrix and find rows and columns that point to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows_with_zero.add(i)  # add rows to rows_with_zero set
                    cols_with_zero.add(j)  # add columns to cols_with_zero

        # iterate over the matrix and manipulate the cells to 0 by checking rows and columns in the set
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows_with_zero:  # if row is in rows_with_zero then set the cell to 0
                    matrix[i][j] = 0
                if j in cols_with_zero:  # if column is in cols_with_zero then set the cell to 0
                    matrix[i][j] = 0
