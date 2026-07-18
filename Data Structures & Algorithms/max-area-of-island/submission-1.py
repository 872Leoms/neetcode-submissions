class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        maxx = 0
        def rec(i,j,temg):
                if i < 0 or i >= rows or j < 0 or j >= cols:
                    return 0
                if grid[i][j] == 0:
                    return 0
                temg[i][j] = 0
                left = rec(i,j-1,temg)
                right = rec(i,j+1,temg)
                top = rec(i-1,j,temg)
                bottom = rec(i+1,j,temg)
                return left + right+top+bottom +1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    temg = grid
                    temp = rec(i,j,temg)
                    if temp > maxx:
                        maxx = temp
        return maxx
        