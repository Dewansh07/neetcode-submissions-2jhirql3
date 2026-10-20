class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        ro = len(matrix)
        co = len(matrix[0])
        l = 0
        r = ro*co -1

        while l<=r:
            mid = (l+r)//2
            row = mid//co
            col = mid%co

            value = matrix[row][col]
            if value == target:
                return True
            elif value >target:
                r = mid-1
            else:
                l = mid+1
        return False