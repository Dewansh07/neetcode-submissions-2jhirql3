class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        original_color = image[sr][sc]

        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or image[r][c]==color or image[r][c]!= original_color:
                return

            image[r][c] = color
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1) 

        if image[sr][sc] != color:
            dfs(sr,sc)
        return image