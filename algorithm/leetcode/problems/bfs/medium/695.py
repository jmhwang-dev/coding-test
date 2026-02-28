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


# again
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        height, width = len(grid), len(grid[0])
        moves = [[0,1], [1,0], [0,-1], [-1, 0]]
        queue = deque()
        result = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] != 1:
                    continue

                area = 0
                grid[row][col] = 0
                queue.append([row, col])

                while queue:
                    cur_row, cur_col = queue.popleft()
                    area += 1
                    for dx, dy in moves:
                        new_row = cur_row + dx
                        new_col = cur_col + dy
                        if (0<=new_row<height) and (0<=new_col<width) and grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 0
                            queue.append([new_row, new_col])
                result = max(result, area)
        return result