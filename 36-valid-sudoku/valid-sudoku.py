class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        matrix_set_1 = set()
        matrix_set_2 = set()
        matrix_set_3 = set()

        row1, row2 = 0, 2
        for i in range(0, len(board), 1):
            row_set = set()
            for j in range(0, len(board[0]), 1):
                if board[i][j] not in row_set and board[i][j] != ".":
                    row_set.add(board[i][j])
                elif board[i][j] != ".":
                    return False
                if board[i][j] not in matrix_set_1 and board[i][j] != "." and 0 <= j <= 2 and row1 <= i <= row2:
                    matrix_set_1.add(board[i][j])
                elif board[i][j] not in matrix_set_2 and board[i][j] != "." and 3 <= j <= 5 and row1 <= i <= row2:
                    matrix_set_2.add(board[i][j])
                elif board[i][j] not in matrix_set_3 and board[i][j] != "." and 6 <= j <= 8 and row1 <= i <= row2:
                    matrix_set_3.add(board[i][j])
                elif board[i][j] != ".":
                    return False
            if i == 2 or i == 5 or i == 8:
                matrix_set_1 = set()
                matrix_set_2 = set()
                matrix_set_3 = set()
                if i == 2:
                    row1, row2 = 3, 5
                elif i == 5:
                    row1, row2 = 6, 8

        for i in range(0, len(board[0]), 1):
            col_set = set()
            for j in range(0, len(board), 1):
                if board[j][i] not in col_set and board[j][i] != ".":
                    col_set.add(board[j][i])
                elif board[j][i] != ".":
                    return False
        return True
