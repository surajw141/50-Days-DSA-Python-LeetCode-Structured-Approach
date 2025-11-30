"""Coding Exercise: Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water."""

def numIslands(grid):
    if not grid:
        return 0
    
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        
        grid[x][y] = '0'  # Mark as visited by sinking the island
        dfs(x+1, y)  # Move down
        dfs(x-1, y)  # Move up
        dfs(x, y+1)  # Move right
        dfs(x, y-1)  # Move left
    
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                islands += 1  # Found an island
    
    return islands

# Example usage:
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(numIslands(grid))  # Output: 3