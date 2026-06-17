class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]

        def dfs(r,c):
            if dp[r][c]:
                return dp[r][c]
            val = matrix[r][c]
            res = 1
            for dr, dc in ((0,1), (1,0), (-1,0), (0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > val:
                    res = max(res, 1 + dfs(nr, nc))
            dp[r][c] = res
            return res

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))
        return ans