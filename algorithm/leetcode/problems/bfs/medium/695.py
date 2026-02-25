from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        result = 0
        width = len(grid[0])
        height = len(grid)
        directions = [[0,1], [1,0], [0,-1], [-1, 0]]
        queue = deque()

        for curr_row in range(height):
            for curr_col in range(width):

                if grid[curr_row][curr_col] == 0:
                    continue

                queue.append([curr_row, curr_col])
                grid[curr_row][curr_col] = 0
                area = 1

                while queue:
                    row, col = queue.popleft()

                    for dx, dy in directions:

                        new_row = row + dx
                        new_col = col + dy

                        if not (0 <= new_row < height) or not (0 <= new_col < width):
                            continue
                        
                        if grid[new_row][new_col] == 1:
                            queue.append([new_row, new_col])
                            grid[new_row][new_col] = 0
                            area += 1

                result = max(result, area)

        return result