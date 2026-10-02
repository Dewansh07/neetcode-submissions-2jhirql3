class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = [set() for i in range(n)]
        col = [set() for h in range(n)]
        sqr = [set() for n in range(n)]

        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val == '.':
                    continue
                sq= (r//3)*3 + c//3

                if val in row[r] or val in col[c] or val in sqr[sq]:
                    return False
                else:
                    row[r].add(val)
                    col[c].add(val)
                    sqr[sq].add(val)
        return True