class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def rec(i,j):
            for k in range(len(matrix[0])):
                if matrix[i][k] != 0:
                    matrix[i][k] = None
            for k in range(len(matrix)):
                if matrix[k][j] != 0:
                    matrix[k][j] = None
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rec(i,j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
