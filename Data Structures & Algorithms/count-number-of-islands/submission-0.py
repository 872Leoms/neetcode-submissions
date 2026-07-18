class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])
        count = 0
        unique = set()
        def rec(i,j):
            if i < 0 or i >= rows or j >= cols or j < 0:
                print(f"out of index {i,j}")
                return
            if grid[i][j] == "0":
                print(grid[i][j])
                print(f"zero {i,j}")
                return
            if (i,j) in unique:
                print(f"in unique {i,j}")
                return
            unique.add((i,j))
            print(f"add in unique {i,j}")
            print(unique)
            rec(i,j-1)
            rec(i,j+1)
            rec(i-1,j)
            rec(i+1,j)
            return
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in unique:
                    print(f"count now {i,j}")
                    count += 1
                    rec(i,j)
        return(count)
        print(unique)