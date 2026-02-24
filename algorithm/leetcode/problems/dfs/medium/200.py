from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        width = len(grid[0])
        height = len(grid)
        result = 0

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        visited_char = '#'
        def dfs(row, col):

            if not (0 <= row < height) or not (0 <= col < width) or grid[row][col] != '1':
                return

            grid[row][col] = visited_char                
            
            for dx, dy in directions:
                dfs(row+dx, col+dy)

        for row in range(height):
            for col in range(width):
                if grid[row][col] == '1':
                    result += 1
                    dfs(row, col)

        return result