class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        dia1 = set()
        dia2 = set()
        res = []

        board = [['.']*n for _ in range(n)]

        def backtrack(row):
            if row == n:
                return res.append([''.join(r) for r in board])

            for col in range(n):
                if col in cols or row-col in dia1 or row+col in dia2:
                    continue
                
                board[row][col] = 'Q'

                cols.add(col)
                dia1.add(row-col)
                dia2.add(row+col)

                backtrack(row+1)
                board[row][col] = '.'
                cols.remove(col)
                dia1.remove(row-col)
                dia2.remove(row+col)


        backtrack(0)
        return res