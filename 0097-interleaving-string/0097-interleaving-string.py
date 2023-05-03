class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def help(i,j,k):
            # print(i,j,k)
            nonlocal s1,s2,s3,n1,n2,n3,dp
            if k>=n3:
                return 1
            if i>=n1 or j>=n2 :
                if i<n1 and s1[i]==s3[k]:
                    return help(i+1,j,k+1)
                if j<n2 and s2[j]==s3[k]:
                    return help(i,j+1,k+1)
                return 0 
            
            
            if dp[i][j][k]!=-1:
                return dp[i][j][k] 
            x=0
            y=0
            if s1[i]==s3[k]:
                # print("yes")
                x=help(i+1,j,k+1)
                
            if s2[j]==s3[k]:
                # print("no")
                y=help(i,j+1,k+1)
                
            dp[i][j][k]=x or y 
            # print(dp)
            return dp[i][j][k]
        n1=len(s1)
        n2=len(s2)
        n3=len(s3)
        if n1+n2!=n3:
            return 0 
        dp=[] 
        for i in range(n1):
            l=[] 
            for j in range(n2):
                l.append([-1]*n3)
            dp.append(l)
        # print(dp)
        res=help(0,0,0)
        # print(dp)
        return res
                
        
        