class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])

        start = next(
            (r,c)
            for r in range(rows)
            for c in range(cols)
            if grid[r][c]==1
        )
        q = deque()
        q.append(start)
        visited = set([start])
        peri = 0

        while q:
            r,c = q.popleft()

            for nr,nc in ([r+1,c], [r-1,c], [r,c+1], [r,c-1]):
                if not (0<=nr<rows and 0<=nc<cols) or grid[nr][nc] == 0:
                    peri +=1
                elif (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((nr,nc))
        return peri

