class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def help(i,n,arr,d):
            if i>=n or i<0 or d[i]==1:
                return 0 
            if arr[i]==0:
                return 1 
            d[i]=1
            if (i+arr[i]<n):
                if help(i+arr[i],n,arr,d):
                    return 1
                
            if (i-arr[i]>=0) :
                if help(i-arr[i],n,arr,d):
                    return 1
            return 0
                
            
        n=len(arr)
        d=[-1]*n
        return help(start,n,arr,d)
            
           
        