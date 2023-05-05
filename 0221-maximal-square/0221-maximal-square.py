class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def helper(r,c):
            nonlocal rows,cols,dp,matrix
            if r>=rows or c>=cols:
                return 0 
            if dp[r][c]!=-1:
                return dp[r][c]
            down=helper(r+1,c)
            right=helper(r,c+1)
            diag=helper(r+1,c+1) 
            dp[r][c]=0 
            if matrix[r][c]=="1":
                dp[r][c]=1+min([down,right,diag]) 
            return dp[r][c]
            
            
        rows=len(matrix) 
        cols=len(matrix[0]) 
        dp=[]
        for i in range(rows):
            dp.append([-1]*cols) 
            
        res=0 
        helper(0,0)
        for i in range(rows):
            for j in range(cols):
                res=max(res,dp[i][j])
        return res*res
        