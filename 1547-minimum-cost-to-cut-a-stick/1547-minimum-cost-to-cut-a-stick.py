class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]
        for i in range(m - 2, -1, -1):
            for j in range(i + 2, m):
                mini = float('inf')
                for k in range(i + 1, j):
                    cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                    mini = min(mini, cost)
                dp[i][j] = mini
        return dp[0][m - 1]
    