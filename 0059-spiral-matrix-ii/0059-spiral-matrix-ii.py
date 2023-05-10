class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result=[] 
        for i in range(n):
            result.append([0]*n)
        # print(result)
        rows=cols=n
        top, bottom, left, right = 0, n-1, 0, n-1
        counter=1
        sq=n*n+1
        while counter<sq: # or while top<=bottom and left<=right
            # print(result)
            for i in range(left, right+1):
                result[top][i]=counter 
                counter+=1
            top += 1
            
            for i in range(top, bottom+1):
                result[i][right]=counter 
                counter+=1
            right -= 1
            
            if top <= bottom:
                for i in range(right, left-1, -1):
                    result[bottom][i]=counter 
                    counter+=1
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result[i][left]=counter 
                    counter+=1
                left += 1
        
        return result