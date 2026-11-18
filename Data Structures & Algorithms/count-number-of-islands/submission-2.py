class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        def search(line, entry):
            seen.add((line, entry))
            if line != 0 and grid[line - 1][entry] == '1' and (line-1, entry) not in seen:
                search(line-1, entry)
            if line != len(grid)-1 and grid[line + 1][entry] == '1' and (line+1, entry) not in seen :
                search(line+1, entry)
            if entry != 0 and grid[line][entry - 1] == '1' and (line, entry-1) not in seen:
                search(line, entry-1)
            if entry != len(grid[line])-1 and grid[line][entry+1] == '1' and (line, entry+1) not in seen:
                search(line, entry+1)
            return (line, entry)

        for line in range(len(grid)):
            for entry in range(len(grid[line])):
                if grid[line][entry] == "1" and (line, entry) not in seen:
                    search(line, entry)
                    islands += 1
        return islands
 






        