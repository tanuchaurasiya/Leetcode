class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])
        
        position_map = defaultdict(list)
        
        row = [0]*m
        column = [0]*n
        
        for i in range(m):
            for j in range(n):
                position_map[mat[i][j]].extend([i,j])
        
        
        for i, ele in enumerate(arr):
            x = position_map[ele][0]
            y = position_map[ele][1]
            row[x]+=1
            column[y]+=1
            
            if row[x] == n or column[y] == m:
                return i

        return 0
        