class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()
        ans = 0

        def dfs(x, y, area):
            if x < 0 or x == m or y < 0 or y == n or grid[x][y]!= 1 or (x, y) in visit:
                return 0
            visit.add((x, y))
            return (1 + dfs(x + 1, y, area) + dfs(x - 1, y, area)
            + dfs(x, y + 1, area) + dfs(x, y - 1, area))

        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c, 0))

        return ans
