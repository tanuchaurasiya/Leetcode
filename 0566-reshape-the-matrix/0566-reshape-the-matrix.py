class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0]) 
        if m==r and n==c:
            return mat 
        res=[]
        temp=[] 
        count=0
        # print(m,n)
        if n*m!=r*c:
            return mat
        if r==1:
            for i in range(m):
                for j in range(n):
                    temp.append(mat[i][j])
            res.append(temp)
            return res
        for i in range(m):
            for j in range(n):
                if count<c:
                    temp.append(mat[i][j])
                    count+=1
                else:
                    res.append(temp)
                    temp=[]
                    temp.append(mat[i][j])
                    count=1
        res.append(temp)
        return res