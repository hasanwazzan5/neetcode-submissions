class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse(coord):
            brothersAndChildren = [coord]

            if grid[coord[0]][coord[1]] == "1":
                grid[coord[0]][coord[1]] = "0"

                if coord[1]+1 < len(grid[0]):
                    brothersAndChildren += traverse((coord[0], coord[1]+1))
                if coord[1]-1 >= 0:
                    brothersAndChildren += traverse((coord[0], coord[1]-1))
                if coord[0]+1 < len(grid):
                    brothersAndChildren += traverse((coord[0]+1, coord[1]))
                if coord[0]-1 >= 0:
                    brothersAndChildren += traverse((coord[0]-1, coord[1]))

            return brothersAndChildren
        
        islands = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands.append(traverse((i,j)))

        #print(islands)
        return len(islands)