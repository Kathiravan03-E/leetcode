class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                new_pos = (i * n + j + k) % total
                new_i = new_pos // n
                new_j = new_pos % n
                ans[new_i][new_j] = grid[i][j]

        return ans