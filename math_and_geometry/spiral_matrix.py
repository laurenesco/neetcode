class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # Need to traverse in spiral order
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        result = []

        while top <= bottom and left <= right:

            # Move left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Move down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Move right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

            # Move up
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result
