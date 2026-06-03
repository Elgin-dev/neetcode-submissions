class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows and columns
        for i in range(9):
            if not self.rowchecker(board[i]):
                return False

            if not self.colchecker(i, board):
                return False

        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.boxchecker(board, row, col):
                    return False

        return True

    def rowchecker(self, row):
        seen = set()

        for i in row:
            if i == '.':
                continue

            if i in seen:
                return False

            seen.add(i)

        return True

    def colchecker(self, col, board):
        seen = set()

        for i in range(9):
            val = board[i][col]

            if val == '.':
                continue

            if val in seen:
                return False

            seen.add(val)

        return True

    def boxchecker(self, board, start_row, start_col):
        seen = set()

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):

                val = board[i][j]

                if val == '.':
                    continue

                if val in seen:
                    return False

                seen.add(val)

        return True