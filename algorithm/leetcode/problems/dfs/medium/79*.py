from typing import List

# - back-tracking
# - dfs

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        word_len = len(word)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(i, j, word_index):

            if word_index == word_len:
                return True

            if i == len(board) or i < 0 or j == len(board[0]) or j < 0:
                return False
            
            if board[i][j] != word[word_index]:
                return False

            origin_char = board[i][j]
            board[i][j] = '#'

            for dx, dy in directions:
                ni, nj = i+dx, j+dy
                if dfs(ni, nj, word_index+1):
                    return True
            board[i][j] = origin_char
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.height = len(board)
        self.width = len(board[0])
        self.word_len = len(word)

        def dfs(row, col, cur_idx):
            if cur_idx == self.word_len:
                return True
            
            if not (0 <= row < self.height) or \
            not (0 <= col < self.width) or \
            board[row][col] != word[cur_idx]:
                return False

            temp = board[row][col]
            board[row][col] = '#'

            found = (dfs(row+1, col, cur_idx + 1) or 
                     dfs(row-1, col, cur_idx + 1) or 
                     dfs(row, col+1, cur_idx + 1) or 
                     dfs(row, col-1, cur_idx + 1))
            
            board[row][col] = temp
            return found

        for r in range(self.height):
            for c in range(self.width):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False