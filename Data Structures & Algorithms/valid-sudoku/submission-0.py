class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = [set() for i in board]
        col = [set() for i in board]
        sq = [set() for i in board]

        for r in range(n):
            for c in range(n):
                val = board[r][c]

                if val == ".":
                    continue

                s = (r//3)*3 + c//3

                if val in row[r] or val in col[c] or val in sq[s]:
                    return False
                row[r].add(val)
                col[c].add(val)
                sq[s].add(val)
        return True