#User function Template for python3
class Solution:
	def matSearch(self,mat, N, M, tar):
		# Complete this function

        
        # print(mat)
        for i in range(n):
            if tar>mat[i][-1]:
                continue
            l=0
            r=m-1
            while l<=r:
                mid=(l+r)//2  
                # print(i,l,r,mid)
                if  mat[i][mid]==tar:
                    return 1
                elif mat[i][mid]>tar:
                    r=mid-1
                else:
                    l=mid+1 
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))
# } Driver Code Ends