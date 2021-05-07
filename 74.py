74. Search a 2D Matrix

class BinarySearch:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # BINARY SEARCH
        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = row *  col - 1

        while l < r:
            mid = (l + r) // 2
            # position of mid map to 2d matrix
            if matrix[mid // col][mid % col] < target:
                l = mid + 1
            else:
                r = mid
        return target == matrix[l//col][l % col]
