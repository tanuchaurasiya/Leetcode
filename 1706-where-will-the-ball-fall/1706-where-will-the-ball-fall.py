class Solution:
    def __init__(self):
        self.res=-1
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def help(i,j,m,n,grid):
            # print(i,j)
            if i==m-1 :
                if j==n-1 and grid[i][j]==1 :
                    return 
                if j==0 and grid[i][j]==-1 :
                    return 
                if grid[i][j]==-1:
                    if j-1>=0 and grid[i][j-1]!=-1:
                        return 
                    self.res=j-1
                else:
                    if j+1<n and grid[i][j+1]!=1:
                        return 
                    self.res=j+1
            
                return 
            if j==n-1 and grid[i][j]==1 :
                return 
            if j==0 and grid[i][j]==-1 :
                return 
                
            if grid[i][j]==1:
                if j+1<n and grid[i][j+1]==-1:
                    # print("yes")
                    return 
                else:
                    help(i+1,j+1,m,n,grid) 
                    
            if grid[i][j]==-1:
                if j-1>=0 and grid[i][j-1]==1:
                    # print("no")
                    return 
                else:
                    help(i+1,j-1,m,n,grid)
        m=len(grid)
        n=len(grid[0])
        if m==1 and n==1:
            return [-1]
        res1=[]
        for j in range(n):
            help(0,j,m,n,grid)
            res1.append(self.res) 
            # print(res1)
            # print("break")
            self.res=-1
        return res1
        