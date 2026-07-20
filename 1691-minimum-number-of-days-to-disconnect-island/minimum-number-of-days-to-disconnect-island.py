class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def countIslands():
            visited = [[False] * n for _ in range(m)]

            def dfs(r, c):
                if r < 0 or r >= m or c < 0 or c >= n:
                    return
                if visited[r][c] or grid[r][c] == 0:
                    return

                visited[r][c] = True

                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        dfs(i, j)

            return islands

        # Already disconnected
        if countIslands() != 1:
            return 0

        # Try removing each land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0

                    if countIslands() != 1:
                        return 1

                    grid[i][j] = 1

        return 2