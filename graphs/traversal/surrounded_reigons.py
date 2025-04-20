DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        cant_be_converted = set()

        is_valid = lambda x, y: 0 <= x < m and 0 <= y < n

        def dfs(x, y):
            cant_be_converted.add((x, y))
            for dx, dy in DIRECTIONS:
                newx, newy = x + dx, y + dy
                if (newx, newy) not in cant_be_converted and is_valid(newx, newy) and board[newx][newy] == 'O':
                    dfs(newx, newy)

        # top boundary
        for i in range(n):
            if board[0][i] == 'O':
                dfs(0, i)
        
        # bottom boundary
        for i in range(n):
            if board[m - 1][i] == 'O':
                dfs(m - 1, i)

        # left boundary
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)

        # right boundary
        for i in range(m):
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)

        # convert surrounded 'O's to 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in cant_be_converted:
                    board[i][j] = 'X'
