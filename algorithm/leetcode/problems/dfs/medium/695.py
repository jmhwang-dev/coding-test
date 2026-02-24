class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        width = len(grid[0])
        height = len(grid)

        result = 0
        directions = [[0,1], [1, 0], [0, -1], [-1, 0]]

        def dfs(row, col):
            if not (0 <= row < height) or not (0 <= col < width) or grid[row][col] != 1:
                return 0

            grid[row][col] = -1
            area = 1
            for dx, dy in directions:
                area += dfs(row+dx, col+dy)

            return area

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 1:
                    result = max(result, dfs(row,col))
        return result