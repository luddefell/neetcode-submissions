class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def numNeighbors(i,j):
            neighbors = 0
            if (j != len(grid[0])-1) and grid[i][j+1] == 1:
                neighbors += 1
            if  j != 0 and grid[i][j-1] == 1:
                neighbors += 1            
            if i != (len(grid)-1) and (grid[i+1][j] == 1):
                neighbors += 1
            if i != 0 and (grid[i-1][j] == 1):
                neighbors += 1
            return neighbors
        
        perim = 0
        for row_index in range(len(grid)):
            for colum_index in range(len(grid[row_index])):
                if grid[row_index][colum_index] == 1:
                    neighbors = numNeighbors(row_index, colum_index)
                    # print(neighbors)
                    perim += 4 - neighbors
                    # print(perim)
        return perim

        

