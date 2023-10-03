class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        The idea is to first swap the elements by just iterating over the upper triangular matrix or the lowe triangular
        matrix. We need to swap matrix[i][j] with matrix of [j][i] where i != j. This is nothing but the transpose of the
        matrix. Now, we just need to reverse the column values per row, and it will give us the desired matrix i.e.
        rotated by 90 degrees clockwise.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # iterating over the upper triangular matrix
        for i in range(0, rows, 1):
            for j in range(i + 1, cols, 1):  # iterate over the columns where j starts from i+1
                # swap the values
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # iterate row wise and reverse the row values
        for row in range(0, rows, 1):
            i, j = 0, cols - 1  # two pointers to reverse the row values
            while i < j:
                temp = matrix[row][j]
                matrix[row][j] = matrix[row][i]
                matrix[row][i] = temp
                i += 1
                j -= 1
