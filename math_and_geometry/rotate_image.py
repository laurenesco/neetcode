# Memory: 7.9 MB•Time: 30ms•Submitted at: 07/21/2026 09:59

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # Transpose the matrix
        for row in range(len(matrix)): # Columns
            for col in range (row+1, len(matrix)): # Rows
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # Reverse the rows
        for row in range(len(matrix)):
            matrix[row].reverse()
