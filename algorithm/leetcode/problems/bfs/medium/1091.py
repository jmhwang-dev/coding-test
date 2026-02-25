from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)

        init_row, init_col, init_dist = 0, 0, 0
        queue = deque([[init_row, init_col, init_dist]])
        grid[init_row][init_col] = 1
        moves = [[1,1], [1,0], [0,1], [1, -1], [-1, 0], [0, -1], [-1, -1], [-1, 1]]

        while queue:
            curr_row, curr_col, total_dist = queue.popleft()
            total_dist += 1

            for dx, dy in moves:
                new_row, new_col = curr_row + dx, curr_col + dy

                if curr_row == n-1 and curr_col == n-1:
                    return total_dist
                
                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                    queue.append([new_row, new_col, total_dist])
                    grid[new_row][new_col] = 1
        return -1