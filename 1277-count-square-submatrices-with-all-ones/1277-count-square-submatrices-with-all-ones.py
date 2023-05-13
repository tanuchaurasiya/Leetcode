class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        def help(i,j): 
            nonlocal m,n,mat,dp 
            if i>=m or j>=n or mat[i][j]==0:
                return 0 
            if dp[i][j]!=-1:
                return dp[i][j]
            res=0 
            right=help(i,j+1)
            diag=help(i+1,j+1)
            down=help(i+1,j)

            dp[i][j]=1+min([right,diag,down]) 
            return dp[i][j] 
        m=len(mat)
        n=len(mat[0])
        res1=0
        dp=[]
        for i in range(m):
            dp.append([-1]*n)
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    res1+=help(i,j)
        return res1
