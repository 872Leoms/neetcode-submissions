class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        sett = set()
        maxx = 0
        def rec(i,j,sett):
                if i < 0 or i >= rows or j < 0 or j >= cols:
                    return 0
                if grid[i][j] == 0:
                    return 0
                if (i,j) in sett:
                     return 0
                sett.add((i,j))
                left = rec(i,j-1,sett)
                right = rec(i,j+1,sett)
                top = rec(i-1,j,sett)
                bottom = rec(i+1,j,sett)
                return left + right+top+bottom +1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    temp = rec(i,j,sett)
                    if temp > maxx:
                        maxx = temp
        return maxx
        