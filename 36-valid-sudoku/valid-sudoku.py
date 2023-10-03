class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        The idea is to first iterate over the matrix row by row and keep a track of nos. appearing in the row. If any of the no. is
        repeating then return False. At the same time, we will prepare 3 different 3X3 matrices and also keep on checking if the
        elements inside the matrices are not repeating. And, at last, we will iterate over the matrix column-wise and check
        if the elements are non-repeating.
        """
        matrix_set_1 = set()  # 1st 3X3 matrix
        matrix_set_2 = set()  # 2nd 3X3 matrix
        matrix_set_3 = set()  # 3rd 3X3 matrix

        start_row, end_row = 0, 2  # we will alter the starting and ending row no. to create different matrices
        for i in range(0, len(board), 1):
            # this row_set will check if a row contains any duplicate or not
            row_set = set()
            # we need to iterate over the columns i.e. 0 -> 8
            for j in range(0, len(board[0]), 1):
                if board[i][j] not in row_set and board[i][j] != ".":
                    row_set.add(board[i][j])
                elif board[i][j] != ".":  # we should return False only if board[i][j] is a valid no. and not "."
                    return False
                # below "if" will prepare the 1st matrix i.e. with rows(i) = start_row to end_row and columns(j) = 0, 1, 2
                if board[i][j] not in matrix_set_1 and board[i][j] != "." and 0 <= j <= 2 and start_row <= i <= end_row:
                    matrix_set_1.add(board[i][j])
                # below "elif" will prepare the 2nd matrix i.e. with rows(i) = start_row to end_row and columns(j) = 3, 4, 5
                elif board[i][j] not in matrix_set_2 and board[i][j] != "." and 3 <= j <= 5 and start_row <= i <= end_row:
                    matrix_set_2.add(board[i][j])
                # below "elif" will prepare the 3rd matrix i.e. with rows(i) = start_row to end_row and columns(j) = 6, 7, 8
                elif board[i][j] not in matrix_set_3 and board[i][j] != "." and 6 <= j <= 8 and start_row <= i <= end_row:
                    matrix_set_3.add(board[i][j])
                # if none of the above "if" or "elif" is True and board[i][j] is a valid no. then return False
                elif board[i][j] != ".":
                    return False
            # if "i" is at the end row of a matrix then set all the matrix set to an empty set for new upcoming matrices
            if i in (2, 5, 8):
                matrix_set_1 = set()
                matrix_set_2 = set()
                matrix_set_3 = set()
                if i == 2:  # if i == 2 then set start_row to 3 and end_row to 5
                    start_row, end_row = 3, 5
                elif i == 5:  # if i == 5 then set start_row to 6 and end_row to 8
                    start_row, end_row = 6, 8

        # the below for loop iterates column-wise and check for the duplicates
        for i in range(0, len(board[0]), 1):
            # this col_set will check if a column contains any duplicate or not
            col_set = set()
            for j in range(0, len(board), 1):
                if board[j][i] not in col_set and board[j][i] != ".":
                    col_set.add(board[j][i])
                elif board[j][i] != ".":
                    return False
        # if no return was made till now that means the sudoku is valid
        return True
