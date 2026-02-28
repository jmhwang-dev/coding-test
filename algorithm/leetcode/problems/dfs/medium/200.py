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



# again
# bfs

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        height, width = len(grid), len(grid[0])
        moves = [[0,1], [1,0], [0,-1], [-1,0]]
        queue = deque()
        result = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] == '1':
                    queue.append([row, col])
                    grid[row][col] = '0'
                
                    while queue:
                        cur_row, cur_col = queue.popleft()

                        for dx, dy in moves:
                            new_row = cur_row + dx
                            new_col = cur_col + dy
                            if (0<=new_row<height) and (0<=new_col<width) and grid[new_row][new_col] == '1':
                                grid[new_row][new_col] = '0'
                                queue.append([new_row, new_col])
                    result += 1
        return result



# dfs
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])
        moves = [[0,1], [1,0], [0,-1], [-1, 0]]
        def dfs(row, col):
            
            for dx, dy in moves:
                new_row = row + dx
                new_col = col + dy
                if (0<=new_row<height) and (0<=new_col<width) and grid[new_row][new_col] == '1':
                    grid[new_row][new_col] = '0'
                    dfs(new_row, new_col)
            return 1
        result = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    result += dfs(row, col)

        return result