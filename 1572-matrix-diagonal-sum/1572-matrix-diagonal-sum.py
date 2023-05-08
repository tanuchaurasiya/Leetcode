class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m=len(mat) 
        n=len(mat[0])
        summ=0
        for i in range(m):
            for j in range(n):
                if i==j:
                    summ+=mat[i][j] 
                    break 
                
            if i!=n-i-1:
                summ+=mat[i][n-i-1]
        return summ