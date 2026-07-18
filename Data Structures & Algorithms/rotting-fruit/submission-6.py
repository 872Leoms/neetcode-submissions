class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        fresh = 0
        queue = []
        visited = []
        size = 0
        timer = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh +=1

        while len(queue):
            size = len(queue)
            for i in range(size):
                rotten = queue[0]
                visited.append(rotten)
                queue = queue[1:]

                left = [rotten[0],rotten[1]-1]
                right = [rotten[0],rotten[1]+1]
                top = [rotten[0]-1,rotten[1]]
                bottom = [rotten[0]+1,rotten[1]]
                neighbor = [left,right,top,bottom] 
                for k in neighbor:
                    if (k[0] >= 0 and k[0] < rows) and (k[1] >= 0 and k[1]<cols):
                        if grid[k[0]][k[1]] == 1:
                                grid[k[0]][k[1]] = 2
                                queue.append(k)
                                fresh -= 1
            if len(queue) > 0:
                 timer+=1
        
        if fresh > 0:
            return -1

        return(timer)





        