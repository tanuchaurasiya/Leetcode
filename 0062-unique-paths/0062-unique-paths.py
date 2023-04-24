class Solution:
    def __init__(self):
        self.count=0 
    def uniquePaths(self, m: int, n: int) -> int:
        def isvalid(i,j,m,n,visited):
            if i<0 or j<0 or i>=m or j>=n or visited[i][j]==1:
                return 0
            return 1 
        def dfs(i,j,m,n,visited,dp):
            if i==m-1 and j==n-1:
                return 1
            
            if isvalid(i,j,m,n,visited):
                if dp[i][j]!=-1:
                    return dp[i][j]
                visited[i][j]=1
                dp[i][j]=dfs(i+1,j,m,n,visited,dp)+dfs(i,j+1,m,n,visited,dp)
                visited[i][j]=0 
                return dp[i][j]
            return 0
        
        visited=[]
        dp=[]
        for i in range(m):
            visited.append([-1]*n)
            dp.append([-1]*n)
        return dfs(0,0,m,n,visited,dp) 
    
            
