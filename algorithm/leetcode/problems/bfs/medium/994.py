from collections import deque
from typing import List

# ans1: append [row, col, time] 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        width, height = len(grid[0]), len(grid)

        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        rotten_oranges = deque()
        fresh_orange_count = 0
        for curr_row in range(height):
            for curr_col in range(width):
                if grid[curr_row][curr_col] == 2:
                    rotten_oranges.append([curr_row, curr_col, 0])
                elif grid[curr_row][curr_col] == 1:
                    fresh_orange_count += 1

        if fresh_orange_count == 0:
            return 0
        
        while rotten_oranges:
            row, col, time = rotten_oranges.popleft()

            for dx, dy in directions:
                adj_row, adj_col = row + dx, col + dy
                
                if not (0 <= adj_row < height) or not (0 <= adj_col < width) or grid[adj_row][adj_col] != 1:
                    continue
                
                fresh_orange_count -= 1
                grid[adj_row][adj_col] = 2
                rotten_oranges.append([adj_row, adj_col, time+1])

        return time if fresh_orange_count == 0 else -1


# ans2: 사이즈 측정 방식

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        width, height = len(grid[0]), len(grid)

        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        rotten_oranges = deque()
        fresh_orange_count = 0
        for curr_row in range(height):
            for curr_col in range(width):
                if grid[curr_row][curr_col] == 2:
                    rotten_oranges.append([curr_row, curr_col])
                elif grid[curr_row][curr_col] == 1:
                    fresh_orange_count += 1

        result = 0
    
        while rotten_oranges and fresh_orange_count > 0:
            for _ in range(len(rotten_oranges)):
                row, col = rotten_oranges.popleft()

                for dx, dy in directions:
                    adj_row, adj_col = row + dx, col + dy
                    
                    if not (0 <= adj_row < height) or not (0 <= adj_col < width) or grid[adj_row][adj_col] != 1:
                        continue
                    
                    fresh_orange_count -= 1
                    grid[adj_row][adj_col] = 2
                    rotten_oranges.append([adj_row, adj_col])
            result += 1
        return result if fresh_orange_count == 0 else -1